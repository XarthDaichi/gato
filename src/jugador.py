from src import dificultad
from src import arbol_decisiones
import random

class Jugador:
    """
    Es una superclase para los tipos de jugador existentes

    Atributos
    ---------
    nombre:str
        Es el nombre que el jugador decida
    letra:str
        La letra asignada al jugador para colocar en el tablero

    Metodos
    -------
    movida(tablero)
        Es el metodo virtual el cual se sobreescribe en clases hijas
    """

    def __init__(self, nombre="", letra=""):
        self.nombre = nombre
        self.letra = letra

    def movida(self, tablero):
        """
        Es el metodo virtual el cual se sobreescribe en clases hijas
        """
        pass


class JugadorHumano(Jugador):
    """
    Hereda de la superclase Jugador y se utiliza para un jugador humano

    Atributos
    ---------
    nombre:str
        Es el nombre que el jugador decida
    letra:str
        La letra asignada al jugador para colocar en el tablero

    Metodos
    -------
    movida(tablero)
        Recibe la posicion en la cual el jugador quiere colocar su jugada y devuelve el tablero actualizado
    """

    def __init__(self, nombre="", letra=""):
        super().__init__(nombre, letra)

    def movida(self, tablero, posicionIngresada):
        """
        Recibe la posicion en la cual el jugador quiere colocar su jugada y devuelve el tablero actualizado

        Parametros
        ----------
        tablero
            Es el tablero actual del juego antes de la jugada

        Retorna
        -------
        tableroNuevo
            Es el tablero actualizado con la jugada incluida
        """
        while True:
            # posicionIngresada = int(input("Ingrese la posicion que quiere ingresar (0-8): "))
            # print("Ingrese la posicion que quiere ingresar (0-8): ")
            # posicionIngresada = dibujador.Dibujador.getPosicion()
            if tablero[posicionIngresada] != ' ':
                print("Posicion ya tiene una letra")
                return tablero
            else:
                tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada + 1:]
                break
        return tableroNuevo


class JugadorCPU(Jugador):
    """
    Hereda de la superclase Jugador y se utiliza para un CPU

    Atributos
    ---------
    dificultad:dificultad
        Es la dificultad elegida por el jugador humano, se saca de la clase enumeradora dificultad
    nombre:str
        Se asigna como CPU
    letra:str
        La letra asignada al CPU para colocar en el tablero

    Metodos
    -------
    movida(tablero)
        Determina la movida a realizar del CPU de acuerdo con su dificultad y devuelve el tablero actualizado
    """

    def __init__(self, letra="", dificultadNueva=1, nombre="CPU"):
        super().__init__(nombre, letra)
        self.dificultad = dificultadNueva
        self.arbol = None

    def movida(self, tablero):
        """
        Determina la movida a realizar del CPU de acuerdo con su dificultad y devuelve el tablero actualizado

        Parametros
        ----------
        tablero
            Es el tablero actual del juego antes de la jugada

        Retorna
        -------
        tableroNuevo
            Es el tablero actualizado con la jugada incluida
        """
        tableroNuevo = tablero
        if self.dificultad is dificultad.Dificultad.facil:
            while True:
                posicionIngresada = random.randint(0, 8)
                if tablero[posicionIngresada] == ' ':
                    tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada + 1:]
                    break
        elif self.dificultad is dificultad.Dificultad.normal:  # TODO modificar dificultad normal para diferenciar entre este y facil
            while True:
                posicionIngresada = random.randint()(0, 8)
                if tablero[posicionIngresada] == ' ':
                    tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada + 1:]
                    break
        elif self.dificultad is dificultad.Dificultad.dificil:
            if tablero == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
                posicionIngresada = random.choice([0, 2, 4, 6, 8])
                tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada + 1:]
            else:
                if self.arbol is None:
                    self.arbol = arbol_decisiones.ArbolDecisiones()
                    self.arbol.generarArbol(self.letra, tablero)
                else: self.arbol.cambiarRaizA(tablero)
                tableroNuevo = self.arbol.minimax()
        elif self.dificultad is dificultad.Dificultad.imposible:
            if tablero == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
                posicionIngresada = random.choice([0, 2, 4, 6, 8])
                tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada:]
            else:
                if self.arbol is None:
                    self.arbol = arbol_decisiones.ArbolDecisiones()
                    self.arbol.generarArbol(self.letra, tablero)
                else: self.arbol.cambiarRaizAImposible(tablero)
                self.arbol.minimaxImposible()
                tableroNuevo = self.arbol.raiz.valor
        return tableroNuevo
