# PEC 4 
**Programación para la Ciencia de Datos.** _Belén Gómez Jiménez._
## Estructura

El proyecto de la **PEC4** está estructurado de la siguiente manera:
```
code/
----- __init__.py
----- data/
---------- nics-firearm-background-checks.csv
---------- us-state-populations.csv
----- modules/
---------- __init__.py
---------- utils.py
---------- processing.py
---------- grouping.py
---------- time_analysis.py
---------- states_analysis.py
---------- maps.py
---------- __init__.py
----- figures/
---------- time_evolution.png
----- maps/
---------- handgun_perc_map.html
---------- longgun_perc_map.html
---------- permit_perc_map.html
----- main.py
----- tests.py
----- setup.py
----- requirements.txt
----- README.md
----- LICENSE.md
```

En `data/` encontramos los `.csv` con los datos necesarios para la realización de la PEC; en `modules/`, los distintos scripts de Python que definen las funciones requeridas en cada ejercicio (`utils.py` para el Ejercicio 1, `processing.py` para el Ejercicio 2, etc.); en `tests.py` hay diversos tests unitarios (concretamente 11), que ponen a prueba algunas de las funciones implementadas; en `figures/` es donde se guarda la gráfica del Ejercicio 4; en `maps` los mapas del Ejercicio 6; `main.py` ejecuta todas las funciones en el orden establecido; `requirements.txt` contiene todas las librerías necesarias; `README.md` y `LICENSE.md` contienen una explicación del proyecto, así como la licencia bajo la que se distribuye. Adicionalmente, se incluye un fichero `setup.py`.

## Ejecución

Los pasos que hay que seguir para ejecutar el código son, dentro del directorio `code/`:
1. Crear un entorno virtual de Python: `python3 -m vent pec4`
2. Activar el entorno virtual: `source pec4/bin/activate`
3. Instalar los **requisitos**:
`pip install -r requirements.txt`
4. Ejecutar el script principal: `python main.py`

### Ejecución de los tests
Para ejecutar los tests (asumiendo que se ha llegado al punto 3 de las instrucciones anteriores):
1. `python -m unittest tests.py`

La explicación de dichos tests puede encontrarse en los comentarios (docstrings) de las funciones del script `tests.py`. 

## Licencia

Este proyecto se distribuye bajo los términos de la Licencia MIT. Consúltese el archivo LICENSE para obtener más detalles.

## Bibliografía
- _Unidad 6: Testing, mantenimiento y despliegue de aplicaciones Python_. Programación para la ciencia de datos. **FUOC**.