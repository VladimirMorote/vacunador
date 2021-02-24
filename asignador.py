import pprint as pprint

class asignador():


    def __init__(self, lista_centros=[], lista_vacunas=[], lista_personas=[]):

        """
        Declaro las estructuras que voy a utilizar para hacer los
        cálculos para la asignación


        """

        # archivo donde guardo el resultado de la asignación de turno
        self.out = open("resultado.txt","w")

        if lista_personas == []:




            f = open( "vacunas.txt", "r" )
            self.lista_vacunas = eval( f.read() )
            f.close()



            f = open( "centros.txt", "r" )
            self.lista_centros = eval( f.read() )
            f.close()



            f = open( "personas.txt", "r" )
            self.json_lista_personas = eval( f.read() )
            f.close()

            print( "\n\n 1 -- Listado de Vacunas disponibles: \n\n", self.lista_vacunas )
            print( "\n\n 2 -- Listado de Centros de Vacunación: \n\n", self.lista_centros )
            print( "\n\n 3 -- Personas con intención de recibir la vacuna: \n\n", self.json_lista_personas )



            """"
            # si al constructor no se le pasan valores, entonces agrego valores de prueba.

            self.json_lista_personas = {
                                            "24918294": ("c1", ["diab,hiper"],40),
                                            "24918295": ("c2", [""], 65),
                                            "24918296": ("c1", ["peso"], 80),

                                        }

            self.lista_personas = [(24918294, "c1", ["diab,hiper"],40),
                              (24918295, "c2", [""],65),
                              (24918296, "c1", ["peso"],80)
                              ]

            self.lista_centros = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"]

            self.lista_vacunas = ["v1", "v2", "v3", "v5", "v6", "v7", "v8", "v9", "v10", "v4",
                             "v11", "v12", "v13", "v15", "v16", "v17", "v18", "v19", "v20", "v14"]
            
            
            
            """

            self.vacunas_asigna_centro = {

            }

            self.json_persona_vacuna_turno = {}
            
            


    def fasigna_vac_centro2(self,centro, cantidad):

        laux = []

        contador = 1

        # todo: arreglar la parada
        while contador <= cantidad:

            if len( self.lista_vacunas ) > contador - 1:
                v = self.lista_vacunas[contador - 1]
                laux.append( v )

            contador += 1

        # remover las vacunas asignadas
        for vv in laux:
            self.lista_vacunas.remove( vv )

        self.vacunas_asigna_centro[centro] = laux
        return self.vacunas_asigna_centro


    def fasina_vac_centro_a_todos(self,cantidad):
        for c in self.lista_centros:
            r = self.fasigna_vac_centro2( c, cantidad )


    def fasigna_persona_vacuna_turno(self, persona):
        """
        Esta tripleta es la que representa a una persona, con el centro
        de vacunanción elegigido y las enfermedades declradas.

        (24918294,"c1",["diab,hiper"]

        """

        centro = self.json_lista_personas[str(persona[0])][0]
        persona = persona


        # me voy a ver las vacunas disponibles en en el centro

        vd = self.vacunas_asigna_centro[centro]

        # tomo la primer vacuna disponible

        if vd != []:

            turno = len( vd )

            vacuna_asignada = vd.pop( 0 )

            self.vacunas_asigna_centro[centro] = vd

            self.json_persona_vacuna_turno[str(persona[0])] = (vacuna_asignada, turno, centro)

        else:
            return "no elemento"

        vout = str( self.json_persona_vacuna_turno )

        self.out.write( vout )

        return "ok"

    def ver_turnos_asignados(self):
        # Retorna el json donde se encentra los datos necesarios para el turno
        # para cada persona
        return self.json_persona_vacuna_turno



    def priorizar(self):
        # arma el listado de personas con prioridades según los siguientes criterios:
        """
        - dependiendo de la eda
        - dependiendo de la cantidad de enfermedades

        fórmula:  edad + cantidad_enfermedades * 5

        Por ejemplo:

        - si Juan tiene 60 años y tiene diabetes, presión y sobrepeso;
        la puntuación que adquiere es: 60 + 15 = 75


        """

        lista = []


        print("\n\n 5 --- \n\n")

        for p in self.json_lista_personas:
            datos = self.json_lista_personas[p]
            edad = datos[2]
            cantidad_enfermedades = len(datos[1])

            valor = edad + cantidad_enfermedades * 5


            lista.append((valor,p))

            men = "Calculando prioridad de vacunación para: \n - DNI: %s \n - " \
                  "Edad: %s \n - Cant. Enfermedades: %s \n - Puntuación: %s \n---------------\n" % (p,edad,cantidad_enfermedades,valor)

            print(men)

        # ordeno la lista segun las prioridades
        # queda ordenada de menor a mayor

        lista_ord = sorted(lista)

        # retorna la lista ordenada

        lista_ord.reverse()

        print("\n\n - Ranking: \n",lista_ord, "\n\n")

        return lista_ord



    def fasignar_turnos_a_todos(self):

        ll = self.priorizar()



        for p in ll:

            pp = self.json_lista_personas[p[1]]

            ppp = (p[1],pp[0],p[1])
            rr = self.fasigna_persona_vacuna_turno(ppp)



    def cargar_archivos(self):

        f = open("vacunas.txt","r")
        self.lista_vacunas = eval(f.read())
        f.close()

        f = open( "centros.txt", "r" )
        self.lista_centros = eval( f.read() )
        f.close()

        f = open( "personas.txt", "r" )
        self.json_lista_personas = eval( f.read() )
        f.close()


    def ver_vacunas_asignadas_a_centros(self):
        print("\n\n 4 ------")
        print("- Lotes de Vacunas asignadas a los Centros de Vacunación:")
        print("")
        pprint.pprint(self.vacunas_asigna_centro)
        print( "-" )
        print( "------" )






















