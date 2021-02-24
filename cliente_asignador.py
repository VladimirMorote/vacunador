import pprint as pprint

from asignador import asignador

vasignador = asignador()

# vasignador.cargar_archivos()

######## Paso 1: asigno las vacunas a los centros

vasignador.fasina_vac_centro_a_todos(3)

# Muestro como se asignan las vacunas a los distintos centros
vasignador.ver_vacunas_asignadas_a_centros()


########## Paso 2: asigno la vacunas a las personas y les doy un turno.

vasignador.fasignar_turnos_a_todos()


######### Paso 3: Ver resultado #######################
# Verifico como quedaron asignados los turnos

r = vasignador.ver_turnos_asignados()

pprint.pprint (r)