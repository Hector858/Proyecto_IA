#libreria unittest
import unittest

#Clase estadosDucha de DuchaAgente.py
from DuchaAgente import estadosDucha

class TestPuertaInteligente(unittest.TestCase):
    """
    Clase que ejecuta las pruebas automáticas.
    
    Métodos:
        test_puerta(): Método que rebisa la ducha inteligente.
    """

    def test_ducha_datosSinError(self):
        """
        Método que prueba la ducha inteligente con datos sin error.
        """

        # Se crea el diccionario con las ubicaciones de la puerta.
        diccionarioUbicaciones = {"Ducha1": "0", "Ducha2": "0", "Ducha3": "0", "Ducha4": "0", "Ducha5": "0", "Ducha6": "0", "Ducha7": "0"}
        
        # Se agrega el estadosDucha la ubicación, estado, costo
        self.assertEqual(estadosDucha(diccionarioUbicaciones, 0, 'Ducha1', '0'), 0) 
        # Se agrega el estadosDucha la ubicación, estado, costo
        self.assertEqual(estadosDucha(diccionarioUbicaciones, 0, 'Ducha3', '1'), 1)
        # Se agrega el estadosDucha la ubicación, estado, costo
        self.assertEqual(estadosDucha(diccionarioUbicaciones, 1, 'Ducha7', '1'), 2) 
          
        


        # Se ejecuta las pruebas. 
if __name__ == '__main__':
    #Se ejecuta el test
    unittest.main(argv=['ignored', '-v'], exit=False)