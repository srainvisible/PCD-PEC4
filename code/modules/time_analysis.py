"""
Análisis temporal.
"""

import matplotlib.pyplot as plt
import pandas as pd


def time_evolution(df: pd.DataFrame, path: str) -> None:
    """
    Crea una gráfica donde el X es el número del año y en el eje y se muestran
    3 series temporales: número total de permits, número total de hand_guns y número total
    de long_guns para cada año.
    :param df: DataFrame
    :param path: Path donde guardar el plot
    :return: None
    """
    # Agrupamos los datos por año
    df_yearly = df.groupby('year')[['permit', 'hand_gun', 'long_gun']].sum().reset_index()

    # Creamos un plot con las 3 series temporales
    plt.figure(figsize=(20, 10))
    plt.plot(df_yearly['year'], df_yearly['permit'], label='Permits', marker='o')
    plt.plot(df_yearly['year'], df_yearly['hand_gun'], label='Handguns', marker='o')
    plt.plot(df_yearly['year'], df_yearly['long_gun'], label='Long Guns', marker='o')

    plt.xticks(df_yearly['year'])
    plt.xlabel('Año')
    plt.ylabel('Registros')
    plt.title('Evolución temporal (1998-2020)')
    plt.legend()
    plt.grid(True)

    # Guardamos el plot
    plt.savefig(path + 'time_evolution.png')
