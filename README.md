# Módulo para la asignación de turnos de vacunación, teniendo en cuenta prioridades de edad, comorbolidad y cercanías geográficas


En este repositorio se presenta un prototipo experimiental, 
de un módulo desarrollado en Pyhon, que implementa la asignación de turnos para 
las personas que hayan registrado su voluntad de vacunarse. 

El algoritmo implementado asigan un turno a cada persona registrada, priorizando la edad, la cantidad 
de comorbilidad y el lugar de vacunación más cercano. 


## Requisitos 

python 3.5, o superior

## Instalación

> git clone https://github.com/wsf/vacunador.git


## Uso 

####  - Paso 1. 

Cagar todas las dosis de vacunas en el archivo **vacunas.txt**

Debe respetar el siguiente formato: 

~~~

["ID_vacun_1", "ID_vacuna_2"]
~~~

Donde **ID_vacuna_x** es una refencia a la dosis de vacuna.

___
#### -  Paso 2. 

Cargar todos los centros de vacunación disponible en el archivo **centros.txt**

Debe respectar el siguiente formato:

~~~

["ID_centro_vacunatorio_1", "ID_centro_vacunatorio_2"]
~~~

Donde **ID_centro_vacunatorio_y** es una referencia a un centro de vacunación esecífico.
___

#### - Paso 3. 

Cargar atodas las personas que manifestaron voluntad de vacunarse.

Se debe respetar el siguiente formato:

~~~

{
    "ID_persona_1": ("ID_centro_vacunación_001", ["enf_001","enf_002","enf_004"],40),
    "ID_persona_2": ("ID_centro_vacunación_002", ["enf_011","enf_005"], 65),
    "ID_persona_3": ("ID_centro_vacunación_001", ["enf_013"], 80)

}

~~~
 
Donde:
 - **ID_persona_x**, es un identificador único de la persona.
 -  **ID_centro_vacunación_x**, es uno de los centros de de vacunación cargados en el paso 2.
 - **enf_00x**, es una de las comorbolidad declarada por la persona.
 - **Los valores numéricos: 40, 65, 80**; son las correspondientes edades declaradas.
 
____


#### - Paso 4. 

Editar el contenido del archivo ***cliente_asignador.py**, en la line 11 se encuentra esta instucción:

~~~
vasignador.fasina_vac_centro_a_todos(3)
~~~  

Donde el número **3**, que recibe la función **fasina_vac_centro_a_todos**, se refiere a la cantidad de dosis que que los centros de vacunación pueden colacar, 
en el período que abarca la asignación de turnos. 

----

#### - Paso 5.

Ejecutar el archivo **cliente_asignador.py**

~~~
python cliente_asignador.py 
~~~~


### - Paso 6.

El resultado de la asignación de turno se guardará en el archivo **resultado.txt**


Descripción de los datos arrojado en el archivo **resultado.txt**


- Primero, muestra los datos obtenidos de los archivos: vacunas.txt, centros.txt, personas.txt

Ejemplo: 
 ~~~
 1 -- Listado de Vacunas disponibles: 

 ['vacuna_001', 'vacuna_002', 'vacuna_003', 'vacuna_004', 'vacuna_004', 'vacuna_005', 'vacuna_006', 'vacuna_007', 'vacuna_008', 'vacuna_009', 'vacuna_010', 'vacuna_011', 'vacuna_012', 'vacuna_013', 'vacuna_014', 'vacuna_015', 'vacuna_016', 'vacuna_017', 'vacuna_018', 'vacuna_019']


 2 -- Listado de Centros de Vacunación: 

 ['centro_vacunación_001', 'centro_vacunación_002', 'centro_vacunación_003', 'centro_vacunación_004', 'centro_vacunación_005', 'centro_vacunación_006', 'centro_vacunación_007', 'centro_vacunación_008', 'centro_vacunación_009']


 3 -- Personas con intención de recibir la vacuna: 

 {'24918294': ('centro_vacunación_001', ['enf_001', 'enf_002', 'enf_004'], 40), '24918295': ('centro_vacunación_002', ['enf_011', 'enf_005'], 65), '24918296': ('centro_vacunación_001', ['enf_013'], 80)}
 ~~~


- Luego, mustra como fueron asignadas las vacunas a cada centro de vacunación

Ejemplo:

~~~
4 ------
- Lotes de Vacunas asignadas a los Centros de Vacunación:

{'centro_vacunación_001': ['vacuna_001', 'vacuna_002', 'vacuna_003'],
 'centro_vacunación_002': ['vacuna_004', 'vacuna_004', 'vacuna_005'],
 'centro_vacunación_003': ['vacuna_006', 'vacuna_007', 'vacuna_008'],
 'centro_vacunación_004': ['vacuna_009', 'vacuna_010', 'vacuna_011'],
 'centro_vacunación_005': ['vacuna_012', 'vacuna_013', 'vacuna_014'],
 'centro_vacunación_006': ['vacuna_015', 'vacuna_016', 'vacuna_017'],
 'centro_vacunación_007': ['vacuna_018', 'vacuna_019'],
 'centro_vacunación_008': [],
 'centro_vacunación_009': []}
-
------
~~~

- Luego, muestra como calcula las prioridades para cada una de las personas, teniendo en cuenta
la edad y las comorbolidades declaradas. 

Ejemplo: 

~~~
5 --- 


Calculando prioridad de vacunación para: 
 - DNI: 24918294 
 - Edad: 40 
 - Cant. Enfermedades: 3 
 - Puntuación: 55 
---------------

Calculando prioridad de vacunación para: 
 - DNI: 24918295 
 - Edad: 65 
 - Cant. Enfermedades: 2 
 - Puntuación: 75 
---------------

Calculando prioridad de vacunación para: 
 - DNI: 24918296 
 - Edad: 80 
 - Cant. Enfermedades: 1 
 - Puntuación: 85 
---------------


 - Ranking: 
 [(85, '24918296'), (75, '24918295'), (55, '24918294')] 
~~~

- Por último, muestra el listado de turnos asignados.

Primero aparece el identificador de las persona, luego se le asocia el centro de vacunación al que debe 
concurrir, junto al turno y la dosis de la vacuna correspondiente.


~~~
{'24918294': ('vacuna_002', 2, 'centro_vacunación_001'),
 '24918295': ('vacuna_004', 3, 'centro_vacunación_002'),
 '24918296': ('vacuna_001', 3, 'centro_vacunación_001')}
~~~
 

