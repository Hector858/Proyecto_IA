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

    def ducha_datosSinError(self):
        """
        Método que prueba la ducha inteligente con datos sin error.
        """

        # Se crea el diccionario con las ubicaciones de la puerta.
        diccionarioUbicaciones = {"Ducha1": "0", "Ducha2": "0", "Ducha3": "0", "Ducha4": "0", "Ducha5": "0", "Ducha6": "0", "Ducha7": "0"}
        

        # Se agrega el estadosDucha la ubicación, estado, costo
        self.assertEqual(estadosDucha('Ducha1', '1', 0,  diccionarioUbicaciones), 1)
        # Se agrega el estado la ubicación, estado, costo
        self.assertEqual(estadosDucha('Ducha3', '0', 0, diccionarioUbicaciones), 0)
        # Se agrega el estado la ubicación, estado, costo
        self.assertEqual(estadosDucha('Ducha7', '1', 0,  diccionarioUbicaciones), 0)
        
    def ducha_valoresIncorrectos(self):
        """
        Este método testea la puerta inteligente con valores erroneos.
        """

        # Se crea el diccionario con las ubicación de las duchas
        diccionarioUbicaciones = {"Ducha1": "0", "Ducha2": "0", "Ducha3": "0", "Ducha4": "0", "Ducha5": "0", "Ducha6": "0", "Ducha7": "0"}

        # Se agrega el estado la ubicación, estado, costo
        self.assertFalse(estadosDucha('Ducha1', '1', 0,  diccionarioUbicaciones), 3)
        # Se agrega el estado la ubicación, estado, costo
        self.assertFalse(estadosDucha('Ducha3', '6', 0, diccionarioUbicaciones), 1)
        # Se agrega el estado la ubicación, estado, costo
        self.assertFalse(estadosDucha('Ducha7', '1', 0, diccionarioUbicaciones), 5)

        # Se ejecuta las pruebas. 
if __name__ == '__main__':
    #Se ejecuta el test
    unittest.main(argv=['ignored', '-v'], exit=False)