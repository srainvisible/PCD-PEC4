"""
Agrupamiento de datos.
"""

import pandas as pd


def groupby_state_and_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula los valores acumulados totales agrupando los datos
    del DataFrame por año y estado (columnas 'year' y 'state').
    :param df: DataFrame original
    :return: DataFrame con los valores acumulados
    """
    df_grouped = df.groupby(['state', 'year'], as_index=False).sum()

    return df_grouped


def print_biggest_handguns(df: pd.DataFrame) -> None:
    """
    Imprime por pantalla un mensaje indicando el nombre del estado y el
    año donde se registraron el mayor número de hand_guns.
    :param df: DataFrame original
    :return: None
    """
    max_handguns = df.loc[df['hand_gun'].idxmax()]

    print(
        f"El mayor número de handguns registrados fue en {max_handguns['state']} en el año {max_handguns['year']} con {max_handguns['hand_gun']} registros.")


def print_biggest_longguns(df: pd.DataFrame) -> None:
    """
    Imprime por pantalla un mensaje indicando el nombre del estado y el
    año donde se registraron el mayor número de long_guns.
    :param df: DataFrame original
    :return: None
    """
    max_longguns = df.loc[df['long_gun'].idxmax()]

    print(
        f"El mayor número de long_guns registrados fue en {max_longguns['state']} en el año {max_longguns['year']} con {max_longguns['long_gun']} registros.")
