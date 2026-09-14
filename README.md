# Actividades_desarrollo_Maestria_Analisis_de_Datos
Este repositorio reúne las actividades, talleres y proyectos prácticos desarrollados en la asignatura de Programación para Analítica de Datos empleando exclusivamente Python. Su propósito es documentar el aprendizaje incremental desde el pensamiento algorítmico y la programación estructurada hasta la creación de clases y pipelines completos de procesamiento ETL con pandas.
# **Estructura del Repositorio**
El contenido se encuentra organizado por módulos de aprendizaje que siguen la progresión conceptual del curso:
* **Módulo 1:** Fundamentos y Estructuras de Control
Paradigma Estructurado: Secuencia, selección y repetición.
Lógica Condicional: Evaluación de proposiciones booleanas con if, elif y else.
Ciclos y Bucles: Iteraciones controladas con for (rangos/secuencias) y while (basados en condición).
Buenas Prácticas: Sintaxis de la indentación de 4 espacios y lógica de orden en condiciones.
* **Módulo 2:** Estructuras de Datos Integradas
Secuencias: Manejo de Listas (mutables) y Tuplas (inmutables por diseño).
Mapeos: Diccionarios (pares clave-valor) para acceso etiquetado.
Manipulación de Colecciones: Métodos de modificación (append, insert, pop), desestructuración/desempaquetado y recorridos limpios con enumerate() e .items().
* **Módulo 3:** Funciones y Modularización
Diseño de Funciones: Definición mediante def, paso de parámetros (posicionales, por nombre y valores por defecto).
Manejo de Retorno: Diferenciación operativa entre print() (mostrar) y return (devolver datos para reutilización).
Alcance de Variables: Gestión de ámbitos globales vs. locales.
* **Módulo 4:** Programación Orientada a Objetos (POO)
Modelado de Entidades: Construcción de clases como planos y creación de instancias/objetos.
Componentes Clave: Uso de __init__, la referencia self, atributos de instancia y de clase, y métodos dunder como __str__.
Pilares POO: Aplicación de Abstracción, Encapsulamiento (atributos privados con __), Herencia (super()) y Polimorfismo.
* **Módulo 5:** Procesamiento de Datos y ETL con pandas
Extract (Extracción): Lectura de fuentes heterogéneas (read_csv, read_excel, read_json, read_sql) configurando codificaciones (encoding='latin-1'), separadores y tipos de datos.
Transform (Transformación):
Diagnóstico sistemático con .info(), .isna(), .duplicated() y .value_counts().
Limpieza de texto mediante el accesor .str (strip, lower, title, replace).
Manejo y parseo de fechas con el accesor .dt y pd.to_datetime().
Tratamiento explícito de nulos (fillna, dropna, imputación por mediana de grupo) y eliminación de duplicados.
Cruce de fuentes con merge() usando validación de cardinalidad (validate='many_to_one') e indicadores.
Remodelación de tablas con concat(), pivot_table() y mel
