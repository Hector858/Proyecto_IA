import sys
def ducha ():
    estado_objetivo={'Ducha1' : '0', 'Ducha2' : '0', 'Ducha3' : '0',
    'Ducha4' : '0', 'Ducha5' : '0', 'Ducha6' : '0', 'Ducha7' : '0', }
    cost=0

    ducha = input("Escriba en que ducha se encuentra: ")
    
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
            print("Lugar del bañó: Ducha1")
            print("Costo actual: " +str(cost))

            if segundo_estado =='1':
                print("La ducha 2 esta apagada")
                print("Se dirige a la ducha 2")
                cost+= 1
                print("Costo actual: "+str(cost))

                estado_objetivo['Ducha2'] = '0'
                cost+=1
                print("La ducha dos esta encendida")
                print("Costo actual: "+str(cost))
            else:
                print("La ducha 2 esta encendida")
                print("Sin acción. Costo actual "+str(cost))

ducha()