lista_personas = [(24918294,"c1",["diab,hiper"]),
                  (24918295,"c2",[""]),
                  (24918296,"c1",["peso"])
                  ]

lista_centros = ["c1","c2","c3","c4","c5","c6","c7","c8","c9"]

lista_vacunas = ["v1","v2","v3","v5","v6","v7","v8","v9","v10","v4",
                 "v11", "v12", "v13", "v15", "v16", "v17", "v18", "v19", "v20", "v14"]


vacunas_asigna_centro = {

}


def fasigna_vac_centro(centro,cantidad):

    laux = []

    for v in lista_vacunas:

        laux.append(v)
        cantidad = cantidad  - 1
        if cantidad == 0:
            break
    vacunas_asigna_centro[centro]=laux
    return vacunas_asigna_centro



def fasigna_vac_centro2(centro,cantidad):

    laux = []

    contador = 1

    # todo: arreglar la parada
    while contador <= cantidad:

        if len(lista_vacunas) > contador-1:
            v = lista_vacunas[contador-1]
            laux.append(v)

        contador += 1

    # remover las vacunas asignadas
    for vv in laux:
        lista_vacunas.remove(vv)


    vacunas_asigna_centro[centro]=laux
    return vacunas_asigna_centro


## clientes de la función


"""
r = fasigna_vac_centro2("c1",3)
print(r)
print(lista_vacunas)
"""


# asigno vacunas a todos los centros que tengo en la lista de centros

for c in  lista_centros:

    r = fasigna_vac_centro2(c,3)

    print(r,"\n")


"""
1. orderna a las personas por su prioridad 
 - a cada persona le pongo un puntaje según sus atributos (edad, enfermedades)
 - ordeno a las personas por su puntaje
 
2. Ya acá tengo a las personas ordenadas por prioridad

3. Tomo una persona y verifico el centro y voy al json  vacunas_asigna_centro, busco el centro
y le doy una vacuna. 

- saco una vacuna de la lista de ese centro
- formo otro json que tenga como key a persona y como datos la vacuna asignada y turno
- el turno lo calculo segun el órden de la vacuna en el vacunas_asigna_centro


"""

json_persona_vacuna_turno = {
    "p1":("v1",3,"c1"),
    "p2":("v2",2,"c1"),
    "p3":("v3",1,"c1")
}


def fasigna_persona_vacuna_turno(persona):
    """
    (24918294,"c1",["diab,hiper"]

    """

    centro = persona[1]
    persona = persona[0]

    # me voy a ver las vacunas disponibles en en el centro

    vd = vacunas_asigna_centro[centro]

    # tomo la primer vacuna disponible

    if vd != []:

        turno = len( vd )

        vacuna_asignada = vd.pop(0)


        vacunas_asigna_centro[centro] = vd

        json_persona_vacuna_turno[persona]= (vacuna_asignada,turno,centro)

    else:
        return "no elemento"


    print(json_persona_vacuna_turno)

    return "ok"



"""

## pruebo
rr = fasigna_persona_vacuna_turno(
    ("24918294","c1",["diab,hiper"])
)

"""


for p in lista_personas:
    rr = fasigna_persona_vacuna_turno(p)