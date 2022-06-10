#Se incorpora la librería
from ast import Break
from asyncio.windows_events import NULL
from queue import Queue
from re import L

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
            
        nodo1 : int 
            Nodo 1 o de inicio
        nodo2 : int
            Nodo 2 o de fin
        peso : int 
            Peso de la arista
            
            Este atributo puede tener un valor opcional (proporcionado por uno mismo)
        nodo_inicio : int  
            Nodo inicial del recorrido
        Métodos
        -------
        __init__(self, numero_de_nodos, dirigido=Treu):
                Constructor de la clase Grafo
        
                Crea el diccionario de la lista de adyacencia seteando cada nodo.
        agregar_arista(self, nodo1, nodo2, peso):
                Método que agrega una arista al grafo.
        
                Si el primer grafo no se encuentra dirigido se pasa al siguiente
        imprimir_lista_adyacencia(self):
                Método que imprime la lista de adyacencia.
        
                Imprime la lista de adyacencia de los nodos por cada una de sus llaves.
        
        def bfs_traversal(self, iniciar_nodo):
                Método que permite recorrer el grafo en anchura.
        
                Genera colas y listas de nodos visitados.
        Main
         -------- 
         __main__
                Main de la clase Grafo
        
                Imprime los nodos nodos asignados y muestra el recorrido
        
        """
        # Constructor
        def __init__(self, numero_de_nodos, dirigido=True):#self es uno mismo
                '''
                Constructor de la clase Grafo
        
                Crea el diccionario de la lista de adyacencia seteando cada nodo.
        
        
                    Parámetros: 
                    ----------
                    numero_nodos: int   
                    Número de nodos que posee el grafo
                   dirigido: boolean 
                    Si el grafo es dirigido (true) o no dirigido (false)
                '''
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
        
            Parámetros:
            ----------
            nodo_inicio : int  
                Nodo inicial del recorrido
        '''
                #Inicializa la lista de los nodos visitados
                #Conjunto vacío de nodos visitados
                visitado = set()
                #Inicializa la cola del grafo
                cola = Queue()

                # Colcoa el nodo inicial a la cola
                cola.put(nodo_inicio)
                # Agrega el nodo inicial a la lista visitada
                visitado.add(nodo_inicio)
                
                # el nodo de inicio no tiene padres
                padre=dict()#
                padre[nodo_inicio]=None#
                
                camino_encontrado = False#
        
                #Realiza un bucle mientras la cola no este vacía
                while not cola.empty():
                        # Saca el primer nodo de la cola
                        nodo_actual = cola.get()
                        #Imprime el nodo actual
                        
                        if nodo_actual == nodo_objetivo:#
                                camino_encontrado = True#
                                break#
                # Realiza un recorrido de toda la lista de adyacencia del nodo actual para el siguiente nodo
                        for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                        #indica que si el nodo siguiente no ha sido visitado
                                if siguiente_nodo not in visitado:
                        #Coloca el siguiente nodo a la cola
                                        cola.put(siguiente_nodo)
                                        padre[siguiente_nodo] = nodo_actual#
                        #Agregar el siguiente nodo a la lista de nodos visitados
                                        visitado.add(siguiente_nodo)
                #Reconstrucción de ruta
                objetivo=[]#
                if camino_encontrado:#
                        objetivo.append(nodo_objetivo)#
                        while padre[nodo_objetivo] is not None:#
                                objetivo.append(padre[nodo_objetivo])#
                                nodo_objetivo=padre[nodo_objetivo]#
                        objetivo.reverse()#
                return objetivo#   
#Main de la clase
if __name__ == "__main__":
        
        '''
                Main de la clase Grafo.
        
                Imprime los nodos nodos asignados y muestra el recorrido.
        
        '''
        # Crea una instancia de la clase "Grafo"
        # Este grafo es no dirigido y tiene 5 nodos
        g = Grafo(20, dirigido=False)
        #Se muestran las opciones para ingresar y reslizar el recorrido para llegar al objetivo
        print("Los puntos turisticos de Santo Domingo de su posible interes son los siguientes: ")
        print("Parque Acuático el Pulpo de Santo: 0  Balneario Las Vegas de Julio Moreno: 1  Río Aquepí: 2")
        print("Parque acuatico El Pulpo: 3  Tinalandia Lodge: 4  Río Otongo: 5")
        print("Río Mapalí: 6  Awakenings Ayahuasca Retreats: 7  Tolón Pelé: 8")
        print("San Gabriel del Baba: 9  Vía Aventura: 10  Monumento Del Indio Colorado: 11")
        print("Parque Zaracay: :  12  Parque de la Juventud y la Familia: 13  Cerro Bombolí: 14")
        print("Monumento Monseñor Emilio Sthele: 15  Parque Natural Jelén Tenka:  16")
        print("Río Cajones Chico: 17  Jardín Botánico Padre Julio Marrero:  18")
        print("Santo Domingo de los Tsáchilas La Concordia: 19")
        #Pide los puntos
        while True:
                try:
                        nodo_inicio = int(input("Ingrese un punto el punto Turistico al que se encuentra: "))
                        nodo_objetivo =int(input("Ingrese un punto el punto Turistico al que se se dirije: "))
                except ValueError:
                        print("Debes escribir un número. Intente De nuevo")
                        continue
                
                if (nodo_inicio>=0 and nodo_inicio<=19) and (nodo_objetivo>=0 and nodo_objetivo<=19):
                        print("Haz colocado mal un punto")
                        break
    
        # Agrega las aristas del grafo
        g.agregar_arista(0,1)# Agrega la arista (0,1) con peso=1
        g.agregar_arista(0,2)# Agrega la arista (0,2) con peso=1
        g.agregar_arista(0,3)# Agrega la arista (1,2) con peso=1
        g.agregar_arista(1,5)# Agrega la arista (1,4) con peso=1
        g.agregar_arista(1,8)# Agrega la arista (2,3) con peso=1
        g.agregar_arista(2,6)# Agrega la arista (2,3) con peso=1
        g.agregar_arista(3,4)# Agrega la arista (2,3) con peso=1
        g.agregar_arista(3, 9)
        g.agregar_arista(4, 9)
        g.agregar_arista(5, 7)
        g.agregar_arista(4,7)# Agrega la arista (0,1) con peso=1
        g.agregar_arista(6,7)# Agrega la arista (0,2) con peso=1
        g.agregar_arista(6,8)# Agrega la arista (1,2) con peso=1
        g.agregar_arista(7,8)# Agrega la arista (1,4) con peso=1
        g.agregar_arista(8,9)# Agrega la arista (2,3) con peso=1
        g.agregar_arista(7,9)# Agrega la arista (2,3) con peso=1
        g.agregar_arista(9,10)# Agrega la arista (2,3) con peso=1
        g.agregar_arista(10, 11)
        g.agregar_arista(10, 12)
        g.agregar_arista(10, 13)
        g.agregar_arista(11, 12)
        g.agregar_arista(11, 14)
        g.agregar_arista(12, 13)
        g.agregar_arista(12, 15)
        g.agregar_arista(13, 16)
        g.agregar_arista(14, 15)
        g.agregar_arista(14, 17)
        g.agregar_arista(14, 18)
        g.agregar_arista(15, 16)
        g.agregar_arista(15, 19)
        g.agregar_arista(16, 19)
    
        # Imprime la lista de adyacencia en el formulario del nodo
        g.imprimir_lista_adyacencia()
    
        #print ("A continuación se muestra el primer recorrido en anchura"
                    #" (empezando por el vértice 0)")
    
        camino_objetivo = []#
        camino_objetivo = g.bfs(nodo_inicio, nodo_objetivo)#
        print(camino_objetivo)#