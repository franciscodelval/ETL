#!/usr/bin/env python
# coding: utf-8

#  

# ##  *GENERACION DE FICHEROS DE METADATOS Y LECTURA DE FORMATOS*

# ####  Francisco del Val Yagüe 

# --------------

# Los metadatos consisten en información que caracteriza datos, describen el contenido, calidad, condiciones, historia, disponibilidad y otras características de los datos. Es decir, datos que describen otros datos.
# 
# Los metadados se caracterizan por:
# 
# * Ser datos altamente estructurados que describen características de los datos, como el contenido, calidad, información y otras circunstancias o atributos.
# 
# * Presentan diferenciaciones que dependerán, en última instancia, de las reglas incluidas en las aplicaciones para determinar la estructura interna de los esquemas de datos.
# 
# * Pueden clasificarse en función de distintos criterios, como su contenido, variabilidad o función. 
# 

# #### FORMATO JSON 

# JSON es un formato de datos basado en texto que sigue la sintaxis de objeto de JavaScript, popularizado por Douglas Crockford. Aunque es muy parecido a la sintaxis de objeto literal de JavaScript, puede ser utilizado independientemente de JavaScript, y muchos entornos de programación poseen la capacidad de leer (convertir; parsear) y generar JSON 

# Un JSON es una cadena cuyo formato recuerda al de los objetos literales JavaScript. Es posible incluir los mismos tipos de datos básicos dentro de un JSON que en un objeto estándar de JavaScript - cadenas, números, arreglos, booleanos, y otros literales de objeto. Esto permite construir una jerarquía de datos, como ésta:

# ##### Ejemplo:

# In[14]:


# Importacion de la libreria 
import json
import pandas as pd


# In[21]:


# visualizacion del fichero formato json
l = open('cm.json', encoding="utf8")
data = json.load(l)
data


# #### FORMATO YAML 

# YAML es un formato de adaptación de datos de forma que sea legible por seres humanos.
# Se inspira en lenguajes como XML, C, Python, Perl, así como el formato para correos electrónicos especificado en RFC 2822.
# Normalmente lo encontraremos con la extensión .yml o incluso .yaml.
# 
# Existen unas reglas generales que deben cumplirse en un documento YAML. Las principales podrían ser las siguientes:
# 
# * Los datos de un documento YAML utilizan caracteres Unicode, UTF-8 ó UTF-16.
# 
# * Los comentarios se realizan utilizando el carácter # dentro de la línea que contiene el comentario.
# 
# * Los caracteres , y ; deben ir seguidos de un espacio en blanco. De esta forma, se podrán representar valores que queramos que tengan esos caracteres.
# 
# * Los espacios en blanco están permitidos, pero no los tabuladores.
# 
# * Las listas comienzan por el caracter – con un valor por cada línea, aunque también se pueden utilizar corchetes [] poniendo los valores dentro de ellos separados por comas , junto con un espacio en blanco.
# 
# * Un vector estará formado por el par clave/valor, estando separados ambos por : poniendo uno por línea, aunque también podemos utilizar {} poniendo cada uno de ellos dentro separados por comas , junto con un espacio en blanco.
# 
# * Se pueden utilizar caracteres de escape \ para representar caracteres especiales.
# 

# ##### Ejemplo

# In[22]:


# importacion de libreria 
import yaml


# In[23]:


# definicion de uan funcion para leer el fichero 
def read_yaml_file(filename):
    with open(filename, 'r') as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)


# In[26]:


students = [{'name': 'Laura', 'occupation': 'student'},
         {'name': 'Francisco', 'occupation': 'student'}]


# In[27]:


with open('students.yaml', 'w') as f:
    
    data = yaml.dump(students, f)


# In[28]:


# lo leemos con la funcion anterior creada
read_yaml_file("students.yaml")


# #### JSON VS YAML

# * YAML, dependiendo de cómo lo use, puede ser más legible que JSON
# 
# * JSON es a menudo más rápido y probablemente aún sea interoperable con más sistemas
# 
# * Es posible escribir un analizador JSON “lo suficientemente bueno” muy rápidamente
# 
# * Las claves duplicadas, que son JSON potencialmente válidas, son definitivamente inválidas YAML.
# 
# * YAML tiene un montón de características, que incluyen comentarios y anclajes relacionales. La syntax de YAML es bastante compleja y puede ser difícil de entender.
# 
# * Es posible escribir estructuras recursivas en yaml: {a: &b [*b]} , que se repetirá infinitamente en algunos convertidores. Incluso con la detección circular, una “bomba yaml” aún es posible (ver bomba xml ).
# 
# * Como no hay referencias, es imposible serializar estructuras complejas con referencias a objetos en JSON. La serialización de YAML puede, por lo tanto, ser más eficiente.
# 

# #### Cuestiones

# ***¿Se pueden leer con spark?***

# El siguiente enclace afirma que sí se puede leer con spark el modelo YAML y explica cómo hacerlo:
#   * https://stackoverflow.com/questions/58806113/how-to-parse-a-yaml-with-spark-scala
#   
# El siguiente enclace afirma que sí se puede leer con spark el modelo JSON y explica cómo hacerlo:
#  * https://sparkbyexamples.com/spark/spark-read-and-write-json-file/

# ***¿Qué tipo de bases de datos No SQL usa estructuras de datos similares?***

# Dependiendo de la forma en la que almacenen la información, nos podemos encontrar varios tipos
# distintos de bases de datos NoSQL.
# 

# ![Captura.PNG](attachment:Captura.PNG)

# #### Bibliografia 

# * https://developer.mozilla.org/es/docs/Learn/JavaScript/Objects/JSON
# * https://geeks.ms/jorge/2019/03/21/yaml-ventajas-desventajas-y-cuando-usarlo/#:~:text=Un%20documento%20YAML%20es%20m%C3%A1s%20peque%C3%B1o%20que%20un%20documento%20JSON,en%20198%20bytes%20en%20YAML.&text=YAML%20es%20un%20superconjunto%20de,o%20mezclar%20un%20documento%20JSON.
# * https://www.dokry.com/9723
# * https://www.diegocalvo.es/leer-json-en-scala/
# * https://www.acens.com/wp-content/images/2014/02/bbdd-nosql-wp-acens.pdf
