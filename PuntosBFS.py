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
    def agregar_arista(self, nodo1, nodo2, peso):
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
    def recorrido_bfs(self, nodo_inicio):
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
        
        #Realiza un bucle mientras la cola no este vacía
        while not cola.empty():
            # Saca el primer nodo de la cola
            nodo_actual = cola.get()
            #Imprime el nodo actual
            print(nodo_actual, end = " ")

            # Realiza un recorrido de toda la lista de adyacencia del nodo actual para el siguiente nodo
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                #indica que si el nodo siguiente no ha sido visitado
                if siguiente_nodo not in visitado:
                    #Coloca el siguiente nodo a la cola
                    cola.put(siguiente_nodo)
                    #Agregar el siguiente nodo a la lista de nodos visitados
                    visitado.add(siguiente_nodo)
            
