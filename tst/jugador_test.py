import unittest
from src import jugador


class JugadorHumanoTestCase(unittest.TestCase):
    def test_constructor(self):
        jugadorTest = jugador.JugadorHumano("Juan", 'X')
        jugadorTest2 = jugador.JugadorHumano()

        self.assertEqual("Juan", jugadorTest.nombre)
        self.assertEqual("X", jugadorTest.letra)
        self.assertEqual("", jugadorTest2.nombre)
        self.assertEqual("", jugadorTest2.letra)
    def test_movida(self):
        jugadorTest = jugador.JugadorHumano("Juan","X")
        tablero = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        tablero2 = jugadorTest.movida(tablero, 1)
        tablero3 = jugadorTest.movida(tablero, 1)
        self.assertEqual(tablero2[0], "X")
        #prueba que al intentar insertar un una posicion ya insertada devuelva el mismo tablero
        self.assertEqual(tablero2[0],tablero3[0])
class JugadorCpuTestCase(unittest.TestCase):
    def test_constructor(self):
        jugadorTest = jugador.JugadorCPU("X", 1)
        self.assertEqual("CPU", jugadorTest.nombre)
        self.assertEqual("X", jugadorTest.letra)
        self.assertEqual(1, jugadorTest.dificultad)


if __name__ == '__main__':
    unittest.main()
