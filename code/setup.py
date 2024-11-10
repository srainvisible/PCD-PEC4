"""
setup.py del proyecto.
"""

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pec4',
    version='1.0.0',
    packages=find_packages(),
    package_data={
        '': ['data/*.csv', 'maps/*.html', 'figures/*.png']
    },
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pec4-main = main:main'
        ]
    },
    author='Belén Gómez Jiménez',
    author_email='bgomezjj@uoc.edu',
    description='Código realizado para la PEC 4 de Programación para la Ciencia de Datos, del Máster de Ciencia de Datos de la UOC.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
)
