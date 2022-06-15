# Se importa la libreria unittest
import unittest

# Se importa la clase Grafo de PuntosBFS.py
from PuntosBFS import Grafo


class TestGrafo(unittest.TestCase):
    """
    Esta clase ejecuta las pruebas unitarias.
    
    Métodos:
        test_grafo(): Testea el grafo.
    """
    
    def test_grafo(self):
        """
        Este método testea la clase Grafo con datos correctos.
        """
        diccionario = {0:"Parque Acuático el Pulpo de Santo",1:"Balneario Las Vegas de Julio Moreno",
                       2:"Río Aquepí",3:"Parque acuatico El Pulpo",4:"Tinalandia Lodge",5:"Río Otongo",
                       6:"Río Mapalí",7:"Awakenings Ayahuasca Retreats",8:"Tolón Pelé",9:"San Gabriel del Baba",
                       10:"Vía Aventura", 11:"Monumento Del Indio Colorado", 12:"Parque Zaracay",
                       12:"Parque de la Juventud y la Familia", 13:"Parque de la Juventud y la Familia", 
                       14:"Cerro Bombolí", 15:"Monumento Monseñor Emilio Sthele", 16:"Parque Natural Jelén Tenka",
                       17:"Río Cajones Chico", 18:"Jardín Botánico Padre Julio Marrero",
                       19:"Santo Domingo de los Tsáchilas La Concordia"}
        
        g = Grafo(20, diccionario)
        
        g.nodos_grafo()
        
        self.assertEquals(g.bfs(1, 9), ['Balneario Las Vegas de Julio Moreno', 'Tolón Pelé', 'San Gabriel del Baba'])
        self.assertEquals(g.bfs(0, 6), ['Parque Acuático el Pulpo de Santo', 'Río Aquepí', 'Río Mapalí'])
        self.assertEquals(g.bfs(3, 14), ['Parque acuatico El Pulpo', 'San Gabriel del Baba', 'Vía Aventura', 'Monumento Del Indio Colorado', 'Cerro Bombolí'])
        
# Ejecucion de las pruebas.
if __name__ == '__main__':
    #Se ejecuta el test
    unittest.main(argv=['ignored', '-v'], exit=False)