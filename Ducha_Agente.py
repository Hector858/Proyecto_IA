#Importamos la libreria sys
#Instrucciones
#INGRESE LA UBICACIÓN Ducha1, Ducha2, Ducha3, Ducha4, Ducha5, Ducha 6, Ducha7
#Ingrese el estado O/1 según corresponda, donde 0 significa encendido y 1 significa apagado
import sys

#Se crea la funcion ducha


def ducha():
    """
    funcion que define a una ducha inteligente 
    para el encendido y apagado por sensor
    """
    #inicializando el ascensor
    #0 indica encendido y 1 indica apagado
    estado_objetivo = {'Ducha1': '0', 'Ducha2': '0', 'Ducha3': '0', 'Ducha4': '0', 'Ducha5': '0', 'Ducha6': '0', 'Ducha7': '0', }
    cost = 0
    #Instrcciones para el usuario
    print("\n************************************************************")
    print("                   --Instrucciones--                          \n")
    print("             Existen 7 locaciones de duchas               \n")
    print("---Ducha1, Ducha2, Ducha3, Ducha4, Ducha5, Ducha6, Ducha7---\n")
    print("                  Existen 2 estados               \n")
    print("      ---0 y 1. Donde 0 es encendido y 1 es apagado---      \n")
    print("************************************************************\n")

    '''
        bloque try con las sentencias que se quiere ejecutar.

        El bloque except se ejecutará cuando el bloque try falle debido a un error.

    '''
    #se ingresa la ubicación de la ducha: Ducha1, Ducha2, Ducha3, Ducha4, Ducha5, Ducha6, Ducha7
    ducha = input("Escriba en que ducha se encuentra: ")
    #se ingresa el estado de la ducha 0/1
    estado = input("Defina el estado de la " + ducha+": ")

    #Realiza un bucle
    while True:
            try:
                #se ingresa la ubicación de la ducha: Ducha1, Ducha2, Ducha3, Ducha4, Ducha5, Ducha6, Ducha7
                ducha = input("Escriba en que ducha se encuentra: ")
                #se ingresa el estado de la ducha 0/1
                estado = input("Defina el estado de la " +ducha+": ")
            #Excepcion de error
            except ValueError:
                #Explicacion del error
                print("Debes ingresar bien los datos")
                continue
            #Si valor de ducha es diferente al valor estavlecido manda alerta
            if (ducha != "Ducha1" and ducha != "Ducha2" and ducha != "Ducha3" and ducha != "Ducha4" and ducha != "Ducha5"
            and ducha != "Ducha6" and ducha != "Ducha7" or estado != "1" and estado != "0"):
                #Alerta por ingresar mal un requerimiento 
                print("Se debe ingresar los datos segun las instrucciones establecidos")
                continue
            else:
                #Termina el ciclo
                break 

    #Realia la condición. Si ducha es igual al parametro establecido 
    if ducha == 'Ducha1':

        # Se estabelce el otro etado de la sigiente ducha
        segundo_estado = input("Defina el otro estado de la Ducha2: ")
        # Se estabelce el otro etado de la sigiente ducha
        tercer_estado = input("Defina el otro estado de la Ducha3: ")
        # Se estabelce el otro etado de la sigiente ducha
        cuarto_estado = input("Defina el otro estado de la Ducha4: ")
        # Se estabelce el otro etado de la sigiente ducha
        quinto_estado = input("Defina el otro estado de la Ducha5: ")
        # Se estabelce el otro etado de la sigiente ducha
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        # Se estabelce el otro etado de la sigiente ducha
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " + str(estado_objetivo))

        print("Usted esta en la ducha 1 ")
        #Condicione si esta apagada la ducha
        if estado == '1':
            print("La ducha no esta encendida")
            estado_objetivo['Ducha1'] = '0'
            cost += 1
            print("Lugar del baño: Ducha1")
            print("Costo actual: " + str(cost))
            #Condicione si esta apagada la ducha
            #Ducha 2
            if segundo_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicion si la ducha encendida
                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if tercer_estado == '1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost += 1
                print("Costo actual: "+str(cost))
                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha3'] = '0'
                cost += 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if quinto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Condicione si esta encendida la ducha1
        if estado == '0':
            print("La ducha 1 esta encendida")

            #Condicione si esta apagada la ducha
            if segundo_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if tercer_estado == '1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha3'] = '0'
                cost += 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if quinto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la ducha
                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Condicione si esta apagada la ducha
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                #Condicione si esta encendida la duchas
                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Realiza la condición si ducha es igual al parametro establecido
    elif ducha == 'Ducha2':
        # Se estabelce el otro etado de la sigiente ducha
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        # Se estabelce el otro etado de la sigiente ducha
        tercer_estado = input("Defina el otro estado de la Ducha3: ")
        # Se estabelce el otro etado de la sigiente ducha
        cuarto_estado = input("Defina el otro estado de la Ducha4: ")
        # Se estabelce el otro etado de la sigiente ducha
        quinto_estado = input("Defina el otro estado de la Ducha5: ")
        # Se estabelce el otro etado de la sigiente ducha
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        # Se estabelce el otro etado de la sigiente ducha
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " + str(estado_objetivo))

        print("Usted esta en la ducha 2 ")
        if estado == '1':
            print("La ducha2 no esta encendida")
            estado_objetivo['Ducha2'] = '0'
            cost += 1
            print("Lugar del baño: Ducha2")
            print("Costo actual: " + str(cost))

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if tercer_estado == '1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost += 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if quinto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha2 esta encendida
        if estado == '0':
            print("La ducha2 esta encendida")

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if tercer_estado == '1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost += 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if quinto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Realiza la condición. Si ducha es igual al parametro establecido
    if ducha == 'Ducha3':
        # Se estabelce el otro etado de la sigiente ducha
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        # Se estabelce el otro etado de la sigiente ducha
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        # Se estabelce el otro etado de la sigiente ducha
        cuarto_estado = input("Defina el otro estado de la Ducha4: ")
        # Se estabelce el otro etado de la sigiente ducha
        quinto_estado = input("Defina el otro estado de la Ducha5: ")
        # Se estabelce el otro etado de la sigiente ducha
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        # Se estabelce el otro etado de la sigiente ducha
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " + str(estado_objetivo))

        print("Usted esta en la ducha 3 ")
        #Ducha 3
        if estado == '1':
            print("La ducha no esta encendida")
            estado_objetivo['Ducha3'] = '0'
            cost += 1
            print("Lugar del baño: Ducha3")
            print("Costo actual: " + str(cost))

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if quinto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha3 esta encendida
        if estado == '0':
            print("La ducha3 esta encendida")

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if quinto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Realiza la condición. Si ducha es igual al parametro establecido
    elif ducha == 'Ducha4':
        # Se estabelce el otro etado de la sigiente ducha
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        # Se estabelce el otro etado de la sigiente ducha
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        # Se estabelce el otro etado de la sigiente ducha
        cuarto_estado = input("Defina el otro estado de la Ducha3: ")
        # Se estabelce el otro etado de la sigiente ducha
        quinto_estado = input("Defina el otro estado de la Ducha5: ")
        # Se estabelce el otro etado de la sigiente ducha
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        # Se estabelce el otro etado de la sigiente ducha
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " + str(estado_objetivo))

        print("Usted esta en la ducha 4 ")
        #Ducha 4
        if estado == '1':
            print("La ducha4 no esta encendida")
            estado_objetivo['Ducha4'] = '0'
            cost += 1
            print("Lugar del baño: Ducha4")
            print("Costo actual: " + str(cost))

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado == '1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost += 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if quinto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha4 esta encendida
        if estado == '0':
            print("La ducha4 esta encendida")

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if quinto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Realiza la condición. Si ducha es igual al parametro establecido
    if ducha == 'Ducha5':
        # Se estabelce el otro etado de la sigiente ducha
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        # Se estabelce el otro etado de la sigiente ducha
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        # Se estabelce el otro etado de la sigiente ducha
        cuarto_estado = input("Defina el otro estado de la Ducha3: ")
        # Se estabelce el otro etado de la sigiente ducha
        quinto_estado = input("Defina el otro estado de la Ducha4: ")
        # Se estabelce el otro etado de la sigiente ducha
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        # Se estabelce el otro etado de la sigiente ducha
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " + str(estado_objetivo))

        print("Usted esta en la ducha 5 ")
        #Ducha 5
        if estado == '1':
            print("La ducha5 no esta encendida")
            estado_objetivo['Ducha5'] = '0'
            cost += 1
            print("Lugar del baño: Ducha5")
            print("Costo actual: " + str(cost))

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado == '1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost += 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if quinto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha5 esta encendida
        if estado == '0':
            print("La ducha5 esta encendida")

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if quinto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Realiza la condición. Si ducha es igual al parametro establecido
    if ducha == 'Ducha6':
        # Se estabelce el otro etado de la sigiente ducha
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        # Se estabelce el otro etado de la sigiente ducha
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        # Se estabelce el otro etado de la sigiente ducha
        cuarto_estado = input("Defina el otro estado de la Ducha3: ")
        # Se estabelce el otro etado de la sigiente ducha
        quinto_estado = input("Defina el otro estado de la Ducha4: ")
        # Se estabelce el otro etado de la sigiente ducha
        sexto_estado = input("Defina el otro estado de la Ducha5: ")
        # Se estabelce el otro etado de la sigiente ducha
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " + str(estado_objetivo))

        print("Usted esta en la ducha 6 ")
        #Ducha 6
        if estado == '1':
            print("La ducha6 no esta encendida")
            estado_objetivo['Ducha6'] = '0'
            cost += 1
            print("Lugar del baño: Ducha6")
            print("Costo actual: " + str(cost))

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado == '1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost += 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if quinto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if sexto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha6 esta encendida
        if estado == '0':
            print("La ducha6 esta encendida")

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if quinto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if sexto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado == '1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost += 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Realiza la condición. Si ducha es igual al parametro establecido
    if ducha == 'Ducha7':
        # Se estabelce el otro etado de la sigiente ducha
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        # Se estabelce el otro etado de la sigiente ducha
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        # Se estabelce el otro etado de la sigiente ducha
        cuarto_estado = input("Defina el otro estado de la Ducha3: ")
        # Se estabelce el otro etado de la sigiente ducha
        quinto_estado = input("Defina el otro estado de la Ducha4: ")
        # Se estabelce el otro etado de la sigiente ducha
        sexto_estado = input("Defina el otro estado de la Ducha5: ")
        # Se estabelce el otro etado de la sigiente ducha
        septimo_estado = input("Defina el otro estado de la Ducha6: ")
        print("La metada deseada es: " + str(estado_objetivo))

        print("Usted esta en la ducha 7 ")
        #Ducha 7
        if estado == '1':
            print("La ducha7 no esta encendida")
            estado_objetivo['Ducha7'] = '0'
            cost += 1
            print("Lugar del baño: Ducha7")
            print("Costo actual: " + str(cost))

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado == '1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost += 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if quinto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if sexto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if septimo_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha7 esta encendida
        if estado == '0':
            print("La ducha7 esta encendida")

            #Ducha 1
            if segundo_estado == '1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost += 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado == '1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost += 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if quinto_estado == '1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost += 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if sexto_estado == '1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost += 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if septimo_estado == '1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost += 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost += 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Ducha completada
    print("Estado objetivo: ")
    #imprime el estado objetivo actualizado
    print(estado_objetivo)
    print("Medición del desempeño:" + str(cost))


ducha()
