#Se incorpora la librería
from queue import Queue

#Se crea la clase Mapa
class Grafo:
        """
        Una clase que representa el algoritmo de búsqueda por anchura
        para recorrer los nodos de un grafo

        ...

         Atributos
        ----------
        numero_de_nodos : int
            indica el número de nodos que va a llevar el grafo
        dirigido : boolean
            Si el grafo se encuentra en dirigido (True) o no dirigido (False)
        diccionario: list
                Almacena el listado de los puntos de interes
            
        nodo1 : int 
            Nodo 1 o de inicio
        nodo2 : int
            Nodo 2 o de fin
        peso : int 
            Peso de la arista
            
            Este atributo puede tener un valor opcional (proporcionado por uno mismo)
        nodo_inicio : int  
            Nodo inicial del recorrido
        nodo_objetivo: int
                Nodo al que se dirije el recorrido
        Métodos
        -------
        __init__(self, numero_de_nodos, diccionario, dirigido=Treu):
                Constructor de la clase Grafo
        
                Crea el diccionario de la lista de adyacencia seteando cada nodo.
        agregar_arista(self, nodo1, nodo2, peso):
                Método que agrega una arista al grafo.
        
                Si el primer grafo no se encuentra dirigido se pasa al siguiente
        imprimir_lista_adyacencia(self):
                Método que imprime la lista de adyacencia.
        
                Imprime la lista de adyacencia de los nodos por cada una de sus llaves.
        
        def bfs(self, iniciar_nodo):
                Método que permite recorrer el grafo en anchura.
        
                Genera colas y listas de nodos visitados.
                
                Establece el camino para llegar al objetivo
        def nodos_grafo(self):
            Se insertan los nodos que conforman el gráfico de los puntos turísticos de Santo Domingo.
                
            Se crea la aristas entre los nodos insertados.
        def ingreso_inicio(nodo_inicio):
            Ingresa el dato del nodo inicio o el punto en el que se encuentra.
                
            Retorna el valor de nodo inicio.
        def ingreso_objetivo(nodo_objetivo):
            Ingresa el dato del nodo objetivo o el punto al que quiere llegar.
                
            Retorna el valor de nodo objetivo.
        def texto(self):
            Muestra los puntos turísticos de interes con su valor.
        
Main
-------- 
__main__
Main del programa 
        
Imprime los nodos nodos asignados y muestra el recorrido
        
        """
        # Constructor
        def __init__(self, numero_de_nodos,diccionario, dirigido=True):#self es uno mismo
                '''
                Constructor de la clase Grafo
        
                Crea el diccionario de la lista de adyacencia seteando cada nodo.
        
        
                    Parámetros: 
                    ----------
                    numero_nodos: int   
                        Número de nodos que posee el grafo
                    dirigido: boolean 
                        Si el grafo es dirigido (true) o no dirigido (false)
                    diccionario: list
                        Almacena el listado de los puntos de interes
                '''
                self.m_diccionario = diccionario#Se define el diccionario
                self.m_numero_de_nodos = numero_de_nodos#El número de nodos
                self.m_nodos = range(self.m_numero_de_nodos)#genera un rango del número de nodos
		
                #Indica dentro del contructor si es dirigido o no dirigido
                self.m_dirigido = dirigido
		
                # Representación grafo - Lista de adyacencia
                # En python esto es un diccionario e implementar una lista de adyacencia
                self.m_lista_adyacencia = {
                node: set() for node in self.m_nodos#Hace un ciclo de repetición en los nodos para setearlos cada uno
                }
        
        # Función que agrega una arista al grafo
        def agregar_arista(self, nodo1, nodo2, peso=1):
                '''
                Método que agrega una arista al grafo.

                Si el primer grafo no se encuentra dirigido se pasa al siguiente
        
                Se definen los nodos y el peso va a hacer un valor opcional (puede ser cualquiera)
        
                    Parámetros:
                    ----------
                    nodo1 : int 
                        Nodo 1 o de inicio
                    nodo2 : int
                        Nodo 2 o de fin
                    peso : int 
                         Peso de la arista
                    
                        Este atributo puede tener un valor opcional (proporcionado por uno mismo)
                '''
                #Agregar una arista del nodo 1 a la lista de adyacencia
                self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        
                #Si el nodo no esta dirigido se agrega la arista al otro nodo
                if not self.m_dirigido:
                #Agregar una arista del nodo 2 de la lista de adyacencia
                        self.m_lista_adyacencia[nodo2].add((nodo1, peso))  
        
        # Función que imprime la representación del grafo
        def imprimir_lista_adyacencia(self):
                ''' 
                Método que imprime la lista de adyacencia por medio de una matriz.
        
                Imprime la lista de adyacencia de los nodos por cada una de sus llaves.
                '''
                #Realiza un recorrido en la lista de adyacencia a través de sus llaves
                for llave in self.m_lista_adyacencia.keys():
                #Imprime cada uno de los nodos que se encuentren en la lista de adyacencia
                #colocan donde se dirigen los nodos y su peso
                        print("nodo", llave, ": ", self.m_lista_adyacencia[llave])
            
        # Función que imprime el recorrido BFS
        def bfs(self, nodo_inicio, nodo_objetivo):#
                '''
                Método que realiza un recorrido del grafo en anchura.
        
                Genera colas y listas de nodos visitados.
        
                Establece el camino para llegar al objetivo
        
                Parámetros:
                ----------
                nodo_inicio : int  
                        Nodo inicial del recorrido
                nodo_objetivo: int
                        Nodo al que se dirije el recorrido
        '''
                #Inicializa la lista de los nodos visitados
                #Conjunto vacío de nodos visitados
                visitado = set()
                #Inicializa la cola del grafo
                cola = Queue()

                # Coloca el nodo inicial a la cola
                cola.put(nodo_inicio)
                # Agrega el nodo inicial a la lista visitada
                visitado.add(nodo_inicio)
                
                # el nodo de inicio no tiene padres
                padre=dict()#Se define el nodo padre de tipo mapa que asocia claves y valores
                #No tiene nodo padre el nodo de inicio va a ser el padre
                padre[nodo_inicio]=None
                #El camino esta vacio
                camino_encontrado = False
        
                #Realiza un bucle mientras la cola no este vacía
                while not cola.empty():
                        # Saca el primer nodo de la cola
                        nodo_actual = cola.get()
                        #Imprime el diccionario del nodo actual
                        print(diccionario[nodo_actual], end = "\n ") 
                        #Si el nodo actual es el nodo objetivo se acaba la busqueda
                        if nodo_actual == nodo_objetivo:
                                #indica que se acabo la busqueda
                                camino_encontrado = True
                                break#cierra el bucle
                        # Realiza un recorrido de toda la lista de adyacencia del nodo actual para el siguiente nodo
                        for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                                #indica que si el nodo siguiente no ha sido visitado
                                if siguiente_nodo not in visitado:
                                        #Coloca el siguiente nodo a la cola
                                        cola.put(siguiente_nodo)
                                        #El siguiente nodo se convierte en el nodo actual
                                        padre[siguiente_nodo] = nodo_actual
                                        #Agregar el siguiente nodo a la lista de nodos visitados
                                        visitado.add(siguiente_nodo)
                #Reconstrucción de ruta
                objetivo=[]#Lista del objetivo
                #Si el camino encontrado se ecuentra
                if camino_encontrado:
                        #Se agrega el nodo objetivo
                        objetivo.append(nodo_objetivo)
                        #Mientras el nodo padre no sea el nodo objetivo
                        while padre[nodo_objetivo] is not None:
                                #Se agrega el nodo al lista el nodo padre
                                objetivo.append(padre[nodo_objetivo])#
                                #Se define el nodo obejtivo como el padre
                                nodo_objetivo=padre[nodo_objetivo]#
                        #Realiza un proceso de reversapara rastear el camino hasta el nodo inicio
                        #Y crear el camino desde el inicio hasta el objetivo
                        objetivo.reverse()
                #Retorna el objetivo
                return objetivo#  
        
        #Método para agregar los nodos a las aristas
        def nodos_grafo(self):
                '''
                Se insertan los nodos que conforman el gráfico de los puntos turísticos de Santo Domingo.
                
                Se crea la aristas entre los nodos insertados.
        
                '''
                #Los valores de cada uno de los nodos y donde se dirijen
                self.agregar_arista(0,1)# Agrega la arista (0,1)
                self.agregar_arista(0,2)# Agrega la arista (0,2)
                self.agregar_arista(0,3)# Agrega la arista (0,3)
                self.agregar_arista(1,5)# Agrega la arista (1,5)
                self.agregar_arista(1,8)# Agrega la arista (1,8)
                self.agregar_arista(2,6)# Agrega la arista (2,6)
                self.agregar_arista(3,4)# Agrega la arista (3,4)
                self.agregar_arista(3,9)# Agrega la arista (3, 9)
                self.agregar_arista(4,9)# Agrega la arista (4, 9)
                self.agregar_arista(5,7)# Agrega la arista (5, 7)
                self.agregar_arista(4,7)# Agrega la arista (4,7)
                self.agregar_arista(6,7)# Agrega la arista ((6,7)
                self.agregar_arista(6,8)# Agrega la arista (6,8)
                self.agregar_arista(7,8)# Agrega la arista (7,8)
                self.agregar_arista(8,9)# Agrega la arista (8,9)
                self.agregar_arista(7,9)# Agrega la arista (7,9)
                self.agregar_arista(9,10)# Agrega la arista (9,10)
                self.agregar_arista(10, 11)# Agrega la arista (10, 11)
                self.agregar_arista(10, 12)# Agrega la arista (10, 12)
                self.agregar_arista(10, 13)# Agrega la arista (10, 13)
                self.agregar_arista(11, 12)# Agrega la arista (11, 12)
                self.agregar_arista(11, 14)# Agrega la arista (11, 14)
                self.agregar_arista(12, 13)# Agrega la arista (12, 13)
                self.agregar_arista(12, 15)# Agrega la arista (12, 15)
                self.agregar_arista(13, 16)# Agrega la arista (13, 16)
                self.agregar_arista(14, 15)# Agrega la arista (14, 15)
                self.agregar_arista(14, 17)# Agrega la arista (14, 17)
                self.agregar_arista(14, 18)# Agrega la arista (14, 18)
                self.agregar_arista(15, 16)# Agrega la arista (15, 16)
                self.agregar_arista(15, 19)# Agrega la arista (15, 19)
                self.agregar_arista(16, 19)# Agrega la arista (16, 19)
                
        #método para ingresar el nodo de inicio        
        def ingreso_inicio(nodo_inicio):
                '''
                Ingresa el dato del nodo inicio o el punto en el que se encuentra.
                
                Retorna el valor de nodo inicio.
                
                Parámetros: 
                    ----------
                    nodo_objetivo: int   
                        Número del punto en el que se encuentra o inicia.
        
                '''
                #Realiza un bucle para ingresar bien los datos
                while True:
                        #Implementa un try except para evitar que se ingresan otro tipo de datos
                        #o se salten el ingreso
                        try:
                        #ingresa el punto de inicio
                                nodo_inicio = int(input("Ingrese un punto el punto Turístico al que se encuentra: "))
                                
                        #Lo que debe de realiza en caso de la excepcion
                        except ValueError:
                                print("Debes escribir un número dentro del Rango del 0 al 19. Intente De nuevo")
                        #Continua con el proceso
                                continue
                        #Condición para no pasar del rango de números
                        if (nodo_inicio<0 or nodo_inicio>19):
                        #Indica que esta fuera del rango
                                print("Numero fuera de rango. Rango: (0, 19)")
                                continue
                        else:
                                
                                return nodo_inicio
                                #Cierra el ciclo retornando el nodo de inicio
                                
        #método para ingresar el nodo objetivo
        def ingreso_objetivo(nodo_objetivo):
                '''
                Ingresa el dato del nodo objetivo o el punto al que quiere llegar.
                
                Retorna el valor de nodo objetivo.
                
                Parámetros: 
                    ----------
                    nodo_objetivo: int   
                        Número del punto al que se quiere llegar.
        
                '''
                #Realiza un bucle para ingresar bien los datos
                while True:
                        #Implementa un try except para evitar que se ingresan otro tipo de datos
                        #o se salten el ingreso
                        try:
                        #Ingresa el punto objetivo
                                nodo_objetivo =int(input("Ingrese un punto el punto Turístico al que se se dirije: "))
                                
                        #Lo que debe de realiza en caso de la excepcion
                        except ValueError:
                                print("Debes escribir un número dentro del Rango del 0 al 19. Intente De nuevo")
                                #Continua con el proceso
                                continue
                        #Condición para no pasar del rango de números
                        if (nodo_objetivo<0 or nodo_objetivo>19):
                        #Indica que esta fuera del rango
                                print("Numero fuera de rango. Rango: (0, 19)")
                                continue
                        else:
                                return nodo_objetivo
                                #Cierra el ciclo retornando el nodo objetivo
                                
        def texto(self):
                '''
                Muestra los puntos turísticos de interes con su valor.
        
                '''
                #Se muestran las opciones para ingresar y reslizar el recorrido para llegar al objetivo
                print("**LOS PUNTOS TURÍSTICOS DE SANTO DOMINGO DE SU POSIBLE INTERÉS** \n")
                print("Parque Acuático el Pulpo de Santo: 0      | Balneario Las Vegas de Julio Moreno: 1          | Río Aquepí: 2")
                print("Parque acuatico El Pulpo: 3               | Tinalandia Lodge: 4                             | Río Otongo: 5")
                print("Río Mapalí: 6                             | Awakenings Ayahuasca Retreats: 7                | Tolón Pelé: 8")
                print("San Gabriel del Baba: 9                   | Vía Aventura: 10                                | Monumento Del Indio Colorado: 11")
                print("Parque Zaracay: :  12                     | Parque de la Juventud y la Familia: 13          | Cerro Bombolí: 14")
                print("Monumento Monseñor Emilio Sthele: 15      | Parque Natural Jelén Tenka:  16                 |Río Cajones Chico: 17 ")
                print("Jardín Botánico Padre Julio Marrero:  18  | Santo Domingo de los TsáchilasLa Concordia: 19  |")
                
#Main del programa
if __name__ == "__main__":
        
        '''
                Main del programa.
        
                Imprime el diccionario con el recorrido.
                
                Mediante opciones muestra los nodos y el recorrido y el camino
                más para llegar al objetivo.
        
        '''
        #Se define los valores del diccionario que va a llevar cada numero
        diccionario = {0:"Parque Acuático el Pulpo de Santo",1:"Balneario Las Vegas de Julio Moreno",
                       2:"Río Aquepí",3:"Parque acuatico El Pulpo",4:"Tinalandia Lodge",5:"Río Otongo",
                       6:"Río Mapalí",7:"Awakenings Ayahuasca Retreats",8:"Tolón Pelé",9:"San Gabriel del Baba",
                       10:"Vía Aventura", 11:"Monumento Del Indio Colorado", 12:"Parque Zaracay",
                       12:"Parque de la Juventud y la Familia", 13:"Parque de la Juventud y la Familia", 
                       14:"Cerro Bombolí", 15:"Monumento Monseñor Emilio Sthele", 16:"Parque Natural Jelén Tenka",
                       17:"Río Cajones Chico", 18:"Jardín Botánico Padre Julio Marrero",
                       19:"Santo Domingo de los Tsáchilas La Concordia"}
        # Crea una instancia de la clase "Grafo"
        # Este grafo es no dirigido y tiene 5 nodos
        g = Grafo(20, diccionario, dirigido=False)
        #Imprimer las opciones
        g.texto()
        #Realiza un bucle para ingresar bien los datos de las opciones que quiere realizar
        while True:
                #Implementa un try except para evitar que se ingresan otro tipo de datos
                #o se salten el ingreso
                try:
                        #opciones paara realizar las acciones
                        opc =int(input("-------------MENÚ-------------\n 1. Mostrar los nodos \n 2. Realizar el recorrido \n 3. Salir \n Ingrese el número de la acción que quiere realizar: "))
                        if opc==1:
                                #Llama a los nodos establecidos
                                g.nodos_grafo()
                                # Imprime la lista de adyacencia en el formulario del nodo
                                g.imprimir_lista_adyacencia()
                                continue
                        elif opc==2:
                                #Llama a los nodos establecidos
                                g.nodos_grafo()
                                #Se obtiene el punto de inicio
                                ingreso_inicio=g.ingreso_inicio()
                                #Se obtiene el punto objetivo
                                ingreso_objetivo=g.ingreso_objetivo()
                                #Se imprime el camino de la ruta entre los puntos de interes
                                camino_objetivo = g.bfs(ingreso_inicio, ingreso_objetivo)
                                #Se imprime los puntos
                                print(camino_objetivo)   
                                continue    
                        elif opc==3:
                                print("Saliendo del programa...")
                                break#cierra el ciclo
                #Lo que debe de realiza en caso de la excepcion
                except ValueError:
                        print("Debes escribir un número de las opciones del 1 al 3. Intente De nuevo")
                        #Continua con el proceso
                        continue
                #Condición para no pasar del rango de números
                if (opc<1 or opc>3):
                        #Indica que esta fuera del rango
                        print("Numero fuera de rango. Rango: (1, 3)")
                        #Continua con el proceso
                        continue
                else:
                        break #cierra el ciclo