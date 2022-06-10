import sys
def ducha ():
    estado_objetivo={'Ducha1' : '0', 'Ducha2' : '0', 'Ducha3' : '0',
    'Ducha4' : '0', 'Ducha5' : '0', 'Ducha6' : '0', 'Ducha7' : '0', }
    cost=0

    ducha = input("Escriba en que ducha se encuentra: ")
    estado = input("Defina el estado de la " +ducha+": ")
    
    if ducha == 'Ducha1':
        segundo_estado = input("Defina el otro estado de la Ducha2: ")
        tercer_estado = input("Defina el otro estado de la Ducha3: ")
        cuarto_estado = input("Defina el otro estado de la Ducha4: ")
        quinto_estado = input("Defina el otro estado de la Ducha5: ")
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " +str(estado_objetivo))
        
        print("Usted esta en la ducha 1 ")
        if estado == '1':
            print("La ducha no esta encendida")
            estado_objetivo ['Ducha1']='0'
            cost+=1
            print("Lugar del baño: Ducha1")
            print("Costo actual: " +str(cost))

            #Ducha 2
            if segundo_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if tercer_estado =='1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost+= 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 5
            if quinto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+=1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
        
        #Ducha1 esta encendida
        if estado =='0':
            print("La ducha 1 esta encendida")

            #Ducha 2
            if segundo_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if tercer_estado =='1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost+= 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 5
            if quinto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+=1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
    
    #Opcion ducha 2
    elif ducha == 'Ducha2':
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        tercer_estado = input("Defina el otro estado de la Ducha3: ")
        cuarto_estado = input("Defina el otro estado de la Ducha4: ")
        quinto_estado = input("Defina el otro estado de la Ducha5: ")
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " +str(estado_objetivo))
        
        print("Usted esta en la ducha 2 ")
        if estado == '1':
            print("La ducha2 no esta encendida")
            estado_objetivo ['Ducha2']='0'
            cost+=1
            print("Lugar del baño: Ducha2")
            print("Costo actual: " +str(cost))

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))


            #Ducha 3
            if tercer_estado =='1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost+= 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 5
            if quinto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+=1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
        
        #Ducha2 esta encendida
        if estado =='0':
            print("La ducha2 esta encendida")

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if tercer_estado =='1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost+= 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 5
            if quinto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+=1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
    
    if ducha == 'Ducha3':
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        cuarto_estado = input("Defina el otro estado de la Ducha4: ")
        quinto_estado = input("Defina el otro estado de la Ducha5: ")
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " +str(estado_objetivo))
        
        print("Usted esta en la ducha 3 ")
        if estado == '1':
            print("La ducha no esta encendida")
            estado_objetivo ['Ducha3']='0'
            cost+=1
            print("Lugar del baño: Ducha3")
            print("Costo actual: " +str(cost))

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 5
            if quinto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+=1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
        
        #Ducha3 esta encendida
        if estado =='0':
            print("La ducha3 esta encendida")

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 4
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 5
            if quinto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+=1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Ducha 4
    elif ducha == 'Ducha4':
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        cuarto_estado = input("Defina el otro estado de la Ducha3: ")
        quinto_estado = input("Defina el otro estado de la Ducha5: ")
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " +str(estado_objetivo))

        print("Usted esta en la ducha 4 ")
        if estado == '1':
            print("La ducha4 no esta encendida")
            estado_objetivo ['Ducha4']='0'
            cost+=1
            print("Lugar del baño: Ducha4")
            print("Costo actual: " +str(cost))

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado =='1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost+= 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 5
            if quinto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+=1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha4 esta encendida
        if estado =='0':
            print("La ducha4 esta encendida")

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 5
            if quinto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+=1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

#Ducha 5
    if ducha == 'Ducha5':
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        cuarto_estado = input("Defina el otro estado de la Ducha3: ")
        quinto_estado = input("Defina el otro estado de la Ducha4: ")
        sexto_estado = input("Defina el otro estado de la Ducha6: ")
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " +str(estado_objetivo))

        print("Usted esta en la ducha 5 ")
        if estado == '1':
            print("La ducha5 no esta encendida")
            estado_objetivo ['Ducha5']='0'
            cost+=1
            print("Lugar del baño: Ducha5")
            print("Costo actual: " +str(cost))

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado =='1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost+= 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if quinto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+=1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha4 esta encendida
        if estado =='0':
            print("La ducha5 esta encendida")

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if quinto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+=1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if sexto_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

#Ducha 6
    if ducha == 'Ducha6':
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        cuarto_estado = input("Defina el otro estado de la Ducha3: ")
        quinto_estado = input("Defina el otro estado de la Ducha4: ")
        sexto_estado = input("Defina el otro estado de la Ducha5: ")
        septimo_estado = input("Defina el otro estado de la Ducha7: ")
        print("La metada deseada es: " +str(estado_objetivo))

        print("Usted esta en la ducha 6 ")
        if estado == '1':
            print("La ducha6 no esta encendida")
            estado_objetivo ['Ducha6']='0'
            cost+=1
            print("Lugar del baño: Ducha6")
            print("Costo actual: " +str(cost))

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado =='1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost+= 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if quinto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+=1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if sexto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+= 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha4 esta encendida
        if estado =='0':
            print("La ducha5 esta encendida")

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if quinto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+=1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if sexto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+= 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 7
            if septimo_estado =='1':
                print("La ducha 7 esta apagada")
                print("Se dirige a la ducha 7")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha7'] = '0'
                cost+= 1
                print("La ducha 7 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 7 esta encendida")
                print("Sin acción. Costo actual "+str(cost))


#Ducha 7
    if ducha == 'Ducha7':
        segundo_estado = input("Defina el otro estado de la Ducha1: ")
        tercer_estado = input("Defina el otro estado de la Ducha2: ")
        cuarto_estado = input("Defina el otro estado de la Ducha3: ")
        quinto_estado = input("Defina el otro estado de la Ducha4: ")
        sexto_estado = input("Defina el otro estado de la Ducha5: ")
        septimo_estado = input("Defina el otro estado de la Ducha6: ")
        print("La metada deseada es: " +str(estado_objetivo))

        print("Usted esta en la ducha 7 ")
        if estado == '1':
            print("La ducha7 no esta encendida")
            estado_objetivo ['Ducha7']='0'
            cost+=1
            print("Lugar del baño: Ducha7")
            print("Costo actual: " +str(cost))

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado =='1':
                print("La ducha 3 esta apagada")
                print("Se dirige a la ducha 3")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha3'] = '0'
                cost+= 1
                print("La ducha 3 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 3 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if quinto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+=1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if sexto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+= 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if septimo_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

        #Ducha7 esta encendida
        if estado =='0':
            print("La ducha7 esta encendida")

            #Ducha 1
            if segundo_estado =='1':
                print("La ducha 1 esta apagada")
                print("Se dirige a la ducha 1")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha1'] = '0'
                cost+= 1
                print("La ducha 1 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 1 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 2
            if tercer_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+= 1
                print("La ducha 2 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 3
            if cuarto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+= 1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))
            
            #Ducha 4
            if quinto_estado =='1':
                print("La ducha 4 esta apagada")
                print("Se dirige a la ducha 4")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha4'] = '0'
                cost+=1
                print("La ducha 4 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 4 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 5
            if sexto_estado =='1':
                print("La ducha 5 esta apagada")
                print("Se dirige a la ducha 5")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha5'] = '0'
                cost+= 1
                print("La ducha 5 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 5 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

            #Ducha 6
            if septimo_estado =='1':
                print("La ducha 6 esta apagada")
                print("Se dirige a la ducha 6")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha6'] = '0'
                cost+= 1
                print("La ducha 6 esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 6 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

    #Ducha completada            
    print("Estado objetivo: ")
    print(estado_objetivo)
    print("Medición del desempeño:"+ str(cost))

ducha()