"""
Lectura y limpieza de datos.
"""

import pandas as pd


def read_csv(path: str) -> pd.DataFrame:
    """
    Lee el fichero .csv y, para comprobar que se han cargado correctamente los datos,
    imprime las 5 primeras filas del DataFrame, así como su estructura.
    :param path: Path del fichero .csv
    :return: DataFrame
    """

    df = pd.read_csv(path)

    print("Primeras 5 filas del DataFrame:")
    print(df.head())

    print("\nEstructura del DataFrame:")
    print(df.info())

    return df


def clean_csv(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    Limpia el DataFrame manteniendo solo las columnas pasadas por parámetro
    e imprime las columnas del DataFrame antes y después de dicha limpieza.
    :param df: DataFrame original
    :param columns: Lista con los nombres de las columnas a mantener
    :return: DataFrame original
    """

    print("Columnas ANTES de la limpieza:")
    print(df.columns)

    df = df[columns]

    print("\nColumnas DESPUÉS de la limpieza:")
    print(df.columns)

    return df


def rename_col(df: pd.DataFrame, column_name: str, new_column_name: str) -> pd.DataFrame:
    """
    Renombra la columna del DataFrame pasada por parámetro (column_name) a new_column_name.
    :param df: DataFrame
    :param column_name: Nombre de la columna a renombrar
    :param new_column_name: Nuevo nombre de la columna a renombrar
    :return: DataFrame con el nombre de la columna modificado
    """

    print("Columnas ANTES de renombrar:")
    print(df.columns)

    if column_name in df.columns:
        df = df.rename(columns={column_name: new_column_name})

    print("\nColumnas DESPUÉS de renombrar:")
    print(df.columns)

    return df
