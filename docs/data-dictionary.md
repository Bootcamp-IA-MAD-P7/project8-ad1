# Diccionario inicial de variables

## Alcance

Este documento describe las 16 variables observadas en los seis datasets de
Airbnb. Se distingue entre el tipo físico inferido por Pandas y el tipo lógico
que corresponde al significado analítico de la variable.

Las definiciones se consideran iniciales: no sustituyen la validación de los
valores ni autorizan todavía transformaciones.

## Fuentes

1. Evidencia observada en los CSV versionados del proyecto.
2. [Inside Airbnb Data Dictionary](https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit?usp=sharing).
3. [Inside Airbnb: Data Assumptions](https://insideairbnb.com/data-assumptions/).

Inside Airbnb es un proyecto independiente y no está respaldado oficialmente
por Airbnb. Cuando una definición no pueda verificarse se indicará como
ambigua, en lugar de completarla por intuición.

## Variables

| Variable | Descripción inicial | Tipo físico observado | Tipo lógico | Función analítica | Unidad o formato | Cobertura observada | Fuente y confianza | Ambigüedades |
|---|---|---|---|---|---|---|---|---|
| `id` | Identificador único del anuncio de Airbnb. | `int64` | Identificador | Clave candidata del alojamiento y enlace entre datos relacionados. | Entero sin unidad. | 100 % en las seis ciudades; 220.031 valores distintos. | Datos observados + Inside Airbnb. Confianza alta. | La unicidad está validada para esta extracción, no para cualquier entrega futura. |
| `host_id` | Identificador de la cuenta del anfitrión o usuario. | `int64` | Identificador | Agrupar anuncios administrados por una misma cuenta. | Entero sin unidad. | 100 % en las seis ciudades; puede repetirse entre anuncios. | Datos observados + Inside Airbnb. Confianza alta. | Una cuenta no debe interpretarse automáticamente como una única persona física. |
| `name` | Título o nombre público del anuncio. | `str` | Texto descriptivo | Etiquetar e identificar visualmente anuncios; posible análisis textual posterior. | Texto libre. | Entre 99,95 % y 100 % según la ciudad. | Datos observados + Inside Airbnb. Confianza alta. | Puede repetirse, cambiar o faltar; no funciona como clave. |
| `host_name` | Nombre público mostrado para el anfitrión. | `str` | Texto descriptivo | Etiqueta de presentación; no identifica de forma fiable una cuenta. | Texto libre. | Entre 97,31 % y 99,99 % según la ciudad. | Datos observados + Inside Airbnb. Confianza alta sobre el campo. | Puede ser nombre personal, conjunto de nombres o denominación comercial; no es único ni siempre está informado. |