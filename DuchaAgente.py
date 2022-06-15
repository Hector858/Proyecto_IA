def estadosDucha(estado_objetivo, cost, ubicacion, estado):
    """
    Parametros
    -----------
        estadoObjetivo (diccionario): Establece el esatdo objetivo en que se encuentran las ducha.
        cost (int): Indica el costo de las acciones realizadas por la ducha.
        ubicacion (str): Indica la ubicacion actual de la ducha.
        estado (str): Indica el estado de la puerta inteligente.
    Retornos:
        cost: Devuelve el costo total de las acciones realizas por la ducha.
    """
    #Asignación del estado objetivo de la ducha
    estado_objetivo = estado_objetivo
    #Asignación del costo actual de la ducha
    cost = cost
    #Asignación de la ubicación actual de la ducha
    ubicacion = ubicacion
    #Asignación del estado de la ducha
    estado = estado
    # Se inicia el control de excepciones
    try:
        #Imprime la ubicacion de la ducha
        print("La ubicación de la ducha es: ", ubicacion)
        #Si el estado es igual a uno
        if estado == '1':
            #Imprime que la ducha esta apagada
            print("La ducha esta apagada")
            #Imprime que la ducha se esta encendiendo
            print("La ducha se esta encendiendo")
            #Se asigna el estado objetivo a la ducha
            estado_objetivo[ubicacion]= '0'
            #Se suma 1 al costo
            cost+=1
            #Imprime que la ducha ya etsa encendida
            print("La ducha esta encendida")
            #Retorna el costo actual de todas las acciones realizadas por la ducha
            return cost
        #Si el esatdo de la ducha es 0 (esta encendida)
        else:
            #Imprime que la ducha esta encendida
            print("La ducha esta encendida")
            #Imprime que no hace ninguna acción
            print("Sin acción. Costo actual: " +str(cost))
            #Retorna el costo
            return cost
    #Termina el control
    except Exception as e:
        #Imprime el mensaje de error
        print(e)

#Se ejecuta el programa
if __name__  == "__main__":
    #Segundo control de excepciones
    try:
        #Creación del diccionario con las 7 ubicaciones de la ducha.
        diccionarioUbicaciones = {"Ducha1": "0", "Ducha2": "0", "Ducha3": "0", "Ducha4": "0", "Ducha5": "0", "Ducha6": "0", "Ducha7": "0"}
        #Inicializamos el costo
        cost = 0
        #Bucle para repetir el ingreso de un  dato mal especificdo por el usuario
        while True:
            #Mensaje en pantalla con las instrucciones para el usuario
            print("\n************************************************************\n                   --Instrucciones--                          \n             Existen 7 locaciones de duchas               \n---Ducha1, Ducha2, Ducha3, Ducha4, Ducha5, Ducha6, Ducha7---\n                  Existen 2 estados               \n      ---0 y 1. Donde 0 es encendido y 1 es apagado---      \n************************************************************")
            #Solicitud de la ubicación actual de la ducha
            ubicacionDucha = input ("Escriba la ubicación de la ducha: ")
            #Si la ubicación de la ducha se encuentra fuera del rango de la duhca
            if ubicacionDucha== "Ducha1" or ubicacionDucha== "Ducha2" or ubicacionDucha== "Ducha3" or ubicacionDucha== "Ducha4" or ubicacionDucha== "Ducha5" or ubicacionDucha== "Ducha6" or ubicacionDucha== "Ducha7":
                #Bucle que controla el mal ingreso del estado de la ducha 
                while True:
                    #Solicitud del estado actual de la ducha
                    estadoDucha = input ("Escriba el estado de la ducha: ")
                    #Si el esatdo ingresado no es igual a 0/1
                    if estadoDucha== "0" or estadoDucha=="1":
                        #Costo es igual a los estados de la Ducha con sus ubicaciones
                        cost = estadosDucha(diccionarioUbicaciones, cost, ubicacionDucha, estadoDucha )
                        #Se imprime el costo
                        print("El costo es: ", cost)
                        #Se repiten instrucciones para recorrer por el diccionario 
                        for clave, valor in diccionarioUbicaciones.items():
                            #Si la ubicación obtenida es igual
                            if clave == ubicacionDucha: 
                                #Imprime que la ducha ya esta encendida
                                print("La ducha ya esta encendida")
                            #Si el esatdo es correcto 
                            else:
                                #Imprime la ubicación de la ducha
                                print("Se encuentra en la ducha: ", clave)
                                #Bucle que recibe un estado valido de la ducha
                                while True:
                                    #Solicitud del estado de la ducha 
                                    estadoDucha = input ("Escriba el estado de la ducha: ")  
                                    #Si el esatdo ingresado es igual a 0/1
                                    if estadoDucha == "1" or estadoDucha=="0":
                                        #Costo es igual a los estados de la Ducha con sus ubicaciones
                                        cost = estadosDucha(diccionarioUbicaciones, cost, clave, estadoDucha )
                                        #Imprime el costo actual
                                        print("El costo es: ", cost)
                                        #Termina de correr el bucle para el ingreso de un estado valido
                                        break
                                    #Si el estado ingresado no es correcto
                                    else:
                                        #Imprime solicitud de revisión de instrucciones y el nuevo ingreso de un esatdo valido
                                        print("Revise las instrucciones. Ingrese un estado valido")
                        #Ducha completada
                        print("Estado objetivo: ")
                        #Imprime el estado objetivo actualizado
                        print(diccionarioUbicaciones)
                        #Imprime la medida de desempeño del Agente
                        print("Medición del desempeño:" + str(cost))
                        #Se termina el bucle 
                        break
                    #Si el esatdo ingresado es incorrecto
                    else:
                        #Imprime que revise las intrucciones y que el esatdo es invalido
                        print("Revise las instrucciones. El estado es invalido")
                #Se termina el bucle para el ingreso de un estado valido
                break
            #Si la ubicación ingresada es incorrecta
            else:
                ##Imprime que revise las intrucciones y que ingrese una ubicación valido
                print("Revise las instrucciones. Debe ingresar una ubicación valida. ")
    #Termina el segundo control
    except Exception as e:
        #Imprime el mensaje de error
        print(e)