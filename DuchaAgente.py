def estadosDucha(estado_objetivo, cost, ubicacion, estado):
    estado_objetivo = estado_objetivo
    cost = cost
    ubicacion = ubicacion
    estado = estado
    try:
        print("La ubicación de la ducha es: ", ubicacion)
        if estado == '1':
            print("La ducha esta apagada")
            print("La ducha se esta encendiendo")
            estado_objetivo[ubicacion]= '0'
            cost+=1
            print("La ducha esta encendida")
            return cost
        else:
            print("La ducha esta encendida")
            print("Sin acción. Costo actual: " +str(cost))
            return cost
    except Exception as e:
        print(e)

if __name__  == "__main__":
    try:
        diccionarioUbicaciones = {"Ducha1": "0", "Ducha2": "0", "Ducha3": "0", "Ducha4": "0", "Ducha5": "0", "Ducha6": "0", "Ducha7": "0",}
        cost = 0
        while True:
            print("\n************************************************************\n                   --Instrucciones--                          \n             Existen 7 locaciones de duchas               \n---Ducha1, Ducha2, Ducha3, Ducha4, Ducha5, Ducha6, Ducha7---\n                  Existen 2 estados               \n      ---0 y 1. Donde 0 es encendido y 1 es apagado---      \n************************************************************")
            ubicacionDucha = input ("Escriba la ubicación de la ducha: ")
            if ubicacionDucha== "Ducha1" or ubicacionDucha== "Ducha2" or ubicacionDucha== "Ducha3" or ubicacionDucha== "Ducha4" or ubicacionDucha== "Ducha5" or ubicacionDucha== "Ducha6" or ubicacionDucha== "Ducha7":
                while True:
                    estadoDucha = input ("Escriba el estado de la ducha: ")
                    if estadoDucha== "0" or estadoDucha=="1":
                        cost = estadosDucha(diccionarioUbicaciones, cost, ubicacionDucha, estadoDucha )
                        print("El costo es: ", cost)
                        for clave, valor in diccionarioUbicaciones.items():
                            if clave == ubicacionDucha: 
                                print("La ducha ya esta encendida")
                            else:
                                print("Se encuentra en la ducha: ", clave)
                                while True:
                                    estadoDucha = input ("Escriba el estado de la ducha: ")  
                                    if estadoDucha == "1" or estadoDucha=="0":
                                        cost = estadosDucha(diccionarioUbicaciones, cost, clave, estadoDucha )
                                        print("El costo es: ", cost)
                                        break
                                    else:
                                        print("Revise las instrucciones. Ingrese un estado valido")
                        #Ducha completada
                        print("Estado objetivo: ")
                        #imprime el estado objetivo actualizado
                        print(diccionarioUbicaciones)
                        print("Medición del desempeño:" + str(cost))
                        
                        break
                    else:
                        print("Revise las instrucciones. El estado es invalido")
                break
            else:
                print("Revise las instrucciones. Debe ingresar una ubicacion valida. ")
    except Exception as e:
        print(e)