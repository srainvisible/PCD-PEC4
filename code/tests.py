"""
Tests unitarios.
"""

import unittest

import pandas as pd

from modules.grouping import groupby_state_and_year
from modules.processing import breakdown_date, erase_month
from modules.states_analysis import groupby_state, clean_states, merge_datasets, calculate_relative_values, \
    handle_outliers
from modules.utils import read_csv, clean_csv, rename_col


class TestUtils(unittest.TestCase):

    def test_read_csv(self) -> pd.DataFrame:
        """
        Comprueba que se lea correctamente el .csv, y que el dataframe
        resultante sea un pd.DataFrame, tenga 14135 filas (las del .csv)
        y las mismas columnas.
        :return: El DataFrame leído
        """
        print("Starting test_read_csv")
        df = read_csv("data/nics-firearm-background-checks.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 14135)
        self.assertListEqual(list(df.columns), ['month', 'state', 'permit', 'permit_recheck', 'handgun',
                                                'long_gun', 'other', 'multiple', 'admin', 'prepawn_handgun',
                                                'prepawn_long_gun', 'prepawn_other', 'redemption_handgun',
                                                'redemption_long_gun', 'redemption_other', 'returned_handgun',
                                                'returned_long_gun', 'returned_other', 'rentals_handgun',
                                                'rentals_long_gun', 'private_sale_handgun', 'private_sale_long_gun',
                                                'private_sale_other', 'return_to_seller_handgun',
                                                'return_to_seller_long_gun',
                                                'return_to_seller_other', 'totals'])
        return df

    def test_clean_csv(self) -> pd.DataFrame:
        """
        Comprueba la limpieza del DataFrame, mirando que las columnas
        resultantes coincidan con las deseadas.
        :return: El DataFrame limpio
        """
        print("Starting test_clean_csv")
        df = self.test_read_csv()
        columns = ['month', 'state', 'permit', 'handgun', 'long_gun']
        df_cleaned = clean_csv(df, columns)
        self.assertListEqual(list(df_cleaned.columns), columns)
        self.assertEqual(len(df_cleaned.columns), 5)
        return df_cleaned

    def test_rename_col(self) -> pd.DataFrame:
        """
        Comprueba que la columna deseada se renombra
        debidamente.
        :return: El DataFrame con la columna renombrada
        """
        print("Starting test_rename_col")
        df_cleaned = self.test_clean_csv()
        df_renamed = rename_col(df_cleaned, 'handgun', 'hand_gun')
        self.assertIn('hand_gun', df_renamed.columns)
        self.assertNotIn('handgun', df_renamed.columns)
        return df_renamed

    def test_breakdown_date(self) -> pd.DataFrame:
        """
        Comprueba que la fecha se divida en dos columnas correctamente,
        y que los valores coincidan con los de la primera fila.
        :return: El DataFrame modificado
        """
        print("Starting test_breakdown_date")
        df_renamed = self.test_rename_col()
        df_broken_down = breakdown_date(df_renamed)
        self.assertIn('year', df_broken_down.columns)
        self.assertIn('month', df_broken_down.columns)
        self.assertEqual(df_broken_down['year'].dtype, int)
        self.assertEqual(df_broken_down['month'].dtype, int)
        self.assertEqual(df_broken_down.iloc[0]['year'], 2020)
        self.assertEqual(df_broken_down.iloc[0]['month'], 3)
        return df_broken_down

    def test_erase_month(self) -> pd.DataFrame:
        """
        Comprueba que la columna 'month' se elimina correctamente.
        :return: El DataFrame con la columna eliminada
        """
        print("Starting test_erase_month")
        df_broken_down = self.test_breakdown_date()
        df_no_month = erase_month(df_broken_down)
        self.assertNotIn('month', df_no_month.columns)
        return df_no_month

    def test_groupby_state_and_year(self) -> pd.DataFrame:
        """
        Comprueba que el DataFrame se agrupa por 'state' y 'year'.
        :return: DataFrame agrupado
        """
        df_no_month = self.test_erase_month()
        grouped_df = groupby_state_and_year(df_no_month)
        self.assertTrue('state' in grouped_df.columns)
        self.assertTrue('year' in grouped_df.columns)
        return grouped_df

    def test_groupby_state(self) -> pd.DataFrame:
        """
        Comprueba que el DataFrame se agrupe solo por 'state'
        :return: DataFrame agrupado
        """
        grouped_df = self.test_groupby_state_and_year()
        grouped_df = groupby_state(grouped_df)
        self.assertTrue('state' in grouped_df.columns)
        self.assertFalse('year' in grouped_df.columns)
        return grouped_df

    def test_clean_states(self) -> pd.DataFrame:
        """
        Comprueba que los estados deseados se eliminan del DataFrame.
        :return: El DataFrame con los estados eliminados
        """
        grouped_df = self.test_groupby_state()
        states = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
        cleaned_df = clean_states(grouped_df, states)
        for state in states:
            self.assertNotIn(state, cleaned_df['state'].values)
        return cleaned_df

    def test_merge_datasets(self) -> pd.DataFrame:
        """
        Comprueba la correcta fusión de dos DataFrames, viendo que una
        columna del nuevo .csv esté en el DataFrame resultante.
        :return: El DataFrame fusionado
        """
        df_cleaned = self.test_clean_states()
        population_df = read_csv("data/us-state-populations.csv")
        merged_df = merge_datasets(df_cleaned, population_df)
        self.assertTrue('pop_2014' in merged_df.columns)
        return merged_df

    def test_calculate_relative_values(self) -> pd.DataFrame:
        """
        Comprueba que se calculan los valores relativos, creándose
        3 nuevas columnas.
        :return: El DataFrame con las 3 nuevas columnas
        """
        merged_df = self.test_merge_datasets()
        df_with_perc = calculate_relative_values(merged_df)
        self.assertTrue('permit_perc' in df_with_perc.columns)
        self.assertTrue('longgun_perc' in df_with_perc.columns)
        self.assertTrue('handgun_perc' in df_with_perc.columns)
        return df_with_perc

    def test_handle_outliers(self) -> pd.DataFrame:
        """
        Comprueba que la media cambia una vez se reemplaza el valor
        de la media de Kentucky.
        :return: El DataFrame sin outliers
        """
        df_with_perc = self.test_calculate_relative_values()
        old_mean = df_with_perc['permit_perc'].mean()
        df_handled_outliers = handle_outliers(df_with_perc)
        new_mean = df_handled_outliers['permit_perc'].mean()
        self.assertNotAlmostEqual(old_mean, new_mean, places=2)
        return df_handled_outliers


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUtils))
unittest.TextTestRunner(verbosity=2).run(suite)
