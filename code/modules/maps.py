"""
Mapas coropléticos.
"""

import folium
import pandas as pd


def create_choropleth_map(df: pd.DataFrame, url: str, variable: str, output_file: str) -> None:
    """
    Crea un mapa coreoplático a partir de un dataframe 'df', cogiendo el mapa de la 'url' y a partir
    de la variable 'variable'. Guarda el mapa en 'output_file'.
    :param df: DataFrame con los datos
    :param url: URL con el mapa 'us-states.json'
    :param variable: Variable a graficar
    :param output_file: Path y nombre del archivo a guardar
    :return: None
    """

    m = folium.Map(location=[40, -95], zoom_start=4)
    state_geo = f"{url}/us-states.json"

    folium.Choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=df,
        columns=['code', variable],
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=.1,
        legend_name=f'{variable}'
    ).add_to(m)
    folium.LayerControl().add_to(m)

    m.save(output_file)
