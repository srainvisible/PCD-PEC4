"""
PEC4 de Programación para la Ciencia de Datos.
"""

import pandas as pd

from modules.grouping import groupby_state_and_year, print_biggest_handguns, print_biggest_longguns
from modules.maps import create_choropleth_map
from modules.processing import breakdown_date, erase_month
from modules.states_analysis import groupby_state, clean_states, merge_datasets, calculate_relative_values, \
    handle_outliers
from modules.time_analysis import time_evolution
from modules.utils import read_csv, clean_csv, rename_col


def exercise_1(file_path: str) -> pd.DataFrame:
    """
    Recibe el path del fichero .csv, lo lee (1.1), selecciona las columnas
    deseadas (1.2) y renombra una columna (1.3).
    :return: DataFrame con los datos modificados
    """

    print('\nEjercicio  1. Lectura y limpieza de los datos -------------')

    print('\n1.1.\n')
    df = read_csv(file_path)

    print('\n1.2.\n')
    columns = ['month', 'state', 'permit', 'handgun', 'long_gun']
    clean_df = clean_csv(df, columns)

    print('\n1.3.\n')

    # NOTA: se modifica 'handgun' por 'hang_gun' en lugar de 'longgun' por 'long_gun', porque este segundo
    # ya tenía ese nombre originalmente
    renamed_df = rename_col(clean_df, 'handgun', 'hand_gun')

    return renamed_df


def exercise_2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recibe un DataFrame, divide la columna de la fecha en 'month' y 'year' (2.1) y
    elimina la columna 'month' (2.2).
    :param df: DataFrame del Ejercicio 1
    :return: DataFrame con las fechas modificadas
    """

    print('\nEjercicio  2. Procesamiento de datos ----------------------')

    print('\n2.1.\n')
    breakdown_date_df = breakdown_date(df)

    print('\n2.2.\n')
    erased_month_df = erase_month(breakdown_date_df)

    return erased_month_df


def exercise_3(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recibe un DataFrame, agrupa los datos por estado y año (3.1),
    imprime el estado y año con mayor número de 'hand_guns' (3.2)
    y lo mismo para 'long_guns' (3.3).
    :param df: DataFrame del Ejercicio 2
    :return: DataFrame con los datos agrupados
    """
    print('\nEjercicio  3. Agrupamiento de datos ----------------------')

    print('\n3.1.\n')
    grouped_by_state_and_year_df = groupby_state_and_year(df)
    print(grouped_by_state_and_year_df)

    print('\n3.2.\n')
    print_biggest_handguns(grouped_by_state_and_year_df)

    print('\n3.3.\n')
    print_biggest_longguns(grouped_by_state_and_year_df)

    return grouped_by_state_and_year_df


def exercise_4(df: pd.DataFrame) -> None:
    """
    Crea un gráfico para el análisis temporal de los datos (4.1)
    y imprime los comentarios al gráfico (4.2).
    :param df: DataFrame con los datos agrupados del Ejercicio 3
    :return: None
    """

    print('\nEjercicio  4. Análisis temporal --------------------------')

    print('\n4.1.\n')
    time_evolution(df, 'figures/')
    print('[Véase la gráfica time_evolution.png en la carpeta /figures].')

    print('\n4.2.\n')
    print('La gráfica muestra una tendencia creciente desde sus inicios (1998) hasta 2018, '
          'tanto en permits, como en long_guns, como en hand_guns (lo que indica una clara correlación). '
          'En 2019, las cifras caen en picado, y siguen decreciendo en 2020. \n'
          'En USA, la pandemia se anunció el 21 de enero de 2020 (de acuerdo con Wikipedia), por '
          'lo que el decrecimiento en el número de permisos en ese año podría explicarse con este hecho. '
          'Sin embargo, desconocemos por qué también hubo una decaída en 2019. \n'
          'Seguramente, los años de pandemia siguieron con una tendencia decreciente, ya que obtener '
          'nuevos permisos debía suponer dificultades burocráticas y logísticas. Una vez normalizada '
          'la situación de pandemia en el país, los números probablemente volvieran a subir (como es de '
          'esperar en USA).')


def exercise_5(df: pd.DataFrame, file_path: str) -> pd.DataFrame:
    """
    Agrupa los datos por estado (5.1), elimina los estados determinados (5.2),
    fusiona los datos del DataFrame de 5.2 y los de un .csv (5.3), calcula los
    valores relativos de 'permit_perc', 'longgun_perc' y 'handgun_perc' (5.4) y calcula
    la media de 'permit_perc' con y sin el estado de Kentucky (5.5).
    :param df: DataFrame con los datos agrupados del Ejercicio 3
    :param file_path: Path del archivo .csv a ser fusionado
    :return: DataFrame con los datos modificados
    """

    print('\nEjercicio  5. Análisis de los estados --------------------')

    print('\n5.1.\n')
    grouped_df = groupby_state(df)

    print('\n5.2.\n')
    states = ['Guam', 'Mariana Islands', 'Puerto Rico', 'Virgin Islands']
    clean_df = clean_states(grouped_df, states)

    print('\n5.3.\n')

    population_df = read_csv(file_path)
    merged_df = merge_datasets(clean_df, population_df)

    print('\n5.4.\n')
    relative_values_df = calculate_relative_values(merged_df)
    print(relative_values_df.head())

    print('\n5.5.\n')
    handled_outliers_df = handle_outliers(relative_values_df)
    print('La media de permit_perc ha cambiado considerablemente tras modificar el valor atípico\n'
          'de la misma del estado de Kentucky. Esto es debido a que el valor de permit_perc para \n'
          'Kentucky era mucho más alto que en el resto de estados, por lo que hacía que la media se \n'
          'disparase. Reemplazándolo, conseguimos que la media represente mejor el conjunto de datos.')

    return handled_outliers_df


def exercise_6(df: pd.DataFrame) -> None:
    """
    Crea mapas coropléticos para las variables 'permit_perc',
    'handgun_perc' y 'longgun_perc', tal como se indica en el
    enunciado del Ejercicio 6.

    :param df: DataFrame con los datos del Ejercicio 5.
    :return: None
    """

    print('\nEjercicio  6. Mapas coropléticos -------------------------')

    url = 'https://raw.githubusercontent.com/python-visualization/folium/main/examples/data'
    create_choropleth_map(df, url, 'permit_perc', 'maps/permit_perc_map.html')
    create_choropleth_map(df, url, 'handgun_perc', 'maps/handgun_perc_map.html')
    create_choropleth_map(df, url, 'longgun_perc', 'maps/longgun_perc_map.html')
    print('[Véanse los mapas generados en la carpeta /maps].')


if __name__ == "__main__":
    file_path_1 = 'data/nics-firearm-background-checks.csv'
    df_1 = exercise_1(file_path_1)
    df_2 = exercise_2(df_1)
    df_3 = exercise_3(df_2)
    exercise_4(df_2)
    file_path_5 = 'data/us-state-populations.csv'
    df_5 = exercise_5(df_3, file_path_5)
    exercise_6(df_5)
