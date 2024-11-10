"""
Análisis de los estados.
"""

import pandas as pd


def groupby_state(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa los datos por estado 'state' y elimina
    la columna 'year'.
    :param df: DataFrame a agrupar
    :return: DataFrame con los datos agrupados
    """

    df_grouped = df.groupby('state', as_index=False).sum()
    df_grouped = df_grouped.drop(columns=['year'])

    print("Primeras 5 filas DESPUÉS de agrupar por estado:")
    print(df_grouped.head())

    return df_grouped


def clean_states(df: pd.DataFrame, states: list[str]) -> pd.DataFrame:
    """
    Elimina los estados de la lista de estados pasada por parámetro, 'states',
    e imprime el número de estados antes y después.
    :param df: DataFrame a modificar
    :param states: Lista de estados a eliminar
    :return: DataFrame con los estados eliminados
    """

    print("Número de estados ANTES de limpiar:", df['state'].nunique())

    df = df[~df['state'].isin(states)]

    print("Número de estados DESPUÉS de limpiar:", df['state'].nunique())

    return df


def merge_datasets(df: pd.DataFrame, population_df: pd.DataFrame) -> pd.DataFrame:
    """
    Fusiona dos DataFrames por estado e imprime las 5 primeras filas.
    :param df: Primer DataFrame a fusionar
    :param population_df: Segundo DataFrame a fusionar
    :return: DataFrame fusionado
    """
    df_merged = pd.merge(df, population_df, how='left', left_on='state', right_on='state')

    print("\nPrimeras 5 filas DESPUÉS de fusionar:")
    print(df_merged.head())

    return df_merged


def calculate_relative_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los valores relativos de 'permit', 'long_gun' y 'hand_gun' y crea
    una nueva columna para cada uno de ellos.
    :param df: DataFrame a modificar
    :return: DataFrame con las tres nuevas columnas
    """

    df['permit_perc'] = (df['permit'] * 100) / df['pop_2014']
    df['longgun_perc'] = (df['long_gun'] * 100) / df['pop_2014']
    df['handgun_perc'] = (df['hand_gun'] * 100) / df['pop_2014']

    return df


def handle_outliers(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula e imprime la media de 'permit_perc', imprime la información del
    estado de Kentucky, reemplaza la media de 'permit_perc' de Kentucky por la
    media general obtenida anteriormente e imprime la nueva media.
    :param df: DataFrame a modificar
    :return: DataFrame modificado
    """

    mean_permit_perc = round(df['permit_perc'].mean(), 2)
    print(f"Media de permit_perc: {mean_permit_perc}")

    kentucky_info = df[df['state'] == 'Kentucky']
    print("\nInformación relativa al estado de Kentucky:")
    for _, row in kentucky_info.iterrows():
        for col, value in row.items():
            print(f"{col}: {value}")

    df.loc[df['state'] == 'Kentucky', 'permit_perc'] = mean_permit_perc

    new_mean_permit_perc = round(df['permit_perc'].mean(), 2)
    print(f"\nMedia de permit_perc DESPUÉS de reemplazar Kentucky: {new_mean_permit_perc}")

    return df
