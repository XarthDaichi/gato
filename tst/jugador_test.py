import unittest
from src import jugador


class JugadorHumanoTestCase(unittest.TestCase):
    def test_herencia(self):
        jugadorTest = jugador.JugadorHumano("Juan", 'X')
        self.assertEqual("Juan", jugadorTest.nombre)
        self.assertEqual("X", jugadorTest.letra)

class JugadorCpuTestCase(unittest.TestCase):
    def test_herencia(self):
        jugadorTest = jugador.JugadorCPU("X", 1)
        self.assertEqual("CPU", jugadorTest.nombre)
        self.assertEqual("", jugadorTest.letra)

if __name__ == '__main__':
    unittest.main()
