import unittest
from src import jugador
from src import dificultad


class JugadorHumanoTestCase(unittest.TestCase):
    """
    Este case son pruebas para Jugador de tipo Humano

    Tests
    -----
    test_constructor()
        Se prueba que la construccion de un jugador humano funcione bien asignandole valores especificos

    test_movida()
        Se prueba que el movimiento realizado por el jugador humano se coloque bien en el tablero
    """
    def test_constructor(self):
        """
        Se prueba que la construccion de un jugador humano funcione bien asignandole valores especificos
        """
        jugadorTest = jugador.JugadorHumano("Juan", 'X')
        jugadorTest2 = jugador.JugadorHumano()

        self.assertEqual("Juan", jugadorTest.nombre)
        self.assertEqual("X", jugadorTest.letra)
        self.assertEqual("", jugadorTest2.nombre)
        self.assertEqual("", jugadorTest2.letra)

    def test_movida(self):
        """
        Se prueba que el movimiento realizado por el jugador humano se coloque bien en el tablero
        """
        jugadorTest = jugador.JugadorHumano("Juan", "X")
        tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        self.assertEqual(jugadorTest.movida(tablero, 1), True)
        # prueba que al intentar insertar un una posicion ya insertada devuelva el mismo tablero
        self.assertEqual(jugadorTest.movida(tablero, 1), False)


class JugadorCpuTestCase(unittest.TestCase):
    """
    Este case son pruebas para Jugador de tipo CPU

    Tests
    -----
    test_constructor()
        Se prueba que la construccion de un jugador CPU funcione bien asignandole valores especificos
    """
    def test_constructor(self):
        """
        Se prueba que la construccion de un jugador CPU funcione bien asignandole valores especificos
        """
        jugadorTest = jugador.JugadorCPU("X", 1)
        self.assertEqual("CPU", jugadorTest.nombre)
        self.assertEqual("X", jugadorTest.letra)
        self.assertEqual(1, jugadorTest.dificultadCPU)

    def test_movida(self):
        tablero = ['O', 'X', 'X', 'X', 'O', 'O', ' ', 'X', ' ']
        jugadorTest = jugador.JugadorCPU('O', dificultad.Dificultad.dificil)
        jugadorTest.movida(tablero)

        self.assertEqual(['O', 'X', 'X', 'X', 'O', 'O', ' ', 'X', 'O'], jugadorTest.movida(tablero))


if __name__ == '__main__':
    unittest.main()
