"""
Procesamiento de datos.
"""

import pandas as pd


def breakdown_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Divide la columna 'month' en dos columnas 'month', con el número
    del mes, y 'year', con el número del año.
    Por ejemplo: month='2020-2' --> month=2 y year=2020
    :param df: DataFrame con la columna 'month'
    :return: DataFrame con la columna 'month' dividida en 'month' y year
    """

    df[['year', 'month']] = df['month'].str.split('-', expand=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)

    print("Primeras 5 filas DESPUÉS de dividir la columna 'month':")
    print(df.head())

    return df


def erase_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina la columna 'month' del DataFrame.
    :param df: DataFrame con la columna 'month'
    :return: DataFrame sin la columna 'month'
    """

    df = df.drop(columns=['month'])

    print("Primeras 5 filas DESPUÉS de eliminar la columna 'month':")
    print(df.head())

    print("\nColumnas del DataFrame DESPUÉS de eliminar la columna 'month':")
    print(df.columns)

    return df
