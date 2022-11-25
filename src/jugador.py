import dificultad, arbol_decisiones
import random


class Jugador:
    def __init__(self, nombre, letra):
        self.nombre = nombre
        self.letra = letra

    def movida(self, tablero):
        pass


class JugadorHumano(Jugador):
    def __init__(self, nombre, letra):
        super().__init__(nombre, letra)

    def movida(self, tablero):
        while True:
            posicionIngresada = int(input("Ingrese la posicion que quiere ingresar (0-8): "))
            if tablero[posicionIngresada] != ' ':
                print("Posicion ya tiene una letra, volver a ingresar")
            else:
                tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada + 1:]
                break
        return tableroNuevo


class JugadorCPU(Jugador):
    def __init__(self, letra, dificultadNueva):
        super().__init__('CPU', letra)
        self.dificultad = dificultadNueva
        self.arbol = None

    def __init__(self, nombre, letra, dificultadNueva):
        super().__init__(nombre, letra)
        self.dificultad = dificultadNueva
        self.arbol = None

    def movida(self, tablero):
        if self.dificultad is dificultad.Dificultad.facil:
            tableroNuevo = tablero
            for c in tablero:
                if c == ' ':
                    movimientoPosible = True
                    break
                else:
                    movimientoPosible = False
            while True:
                posicionIngresada = random.randint(0, 8)
                if tablero[posicionIngresada] == ' ':
                    tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada + 1:]
                    break
        if self.dificultad is dificultad.Dificultad.normal:  # TODO modificar dificultad normal para diferenciar entre este y facil
            while True:
                posicionIngresada = random.randint()(0, 8)
                if tablero[posicionIngresada] == ' ':
                    tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada + 1:]
                    break
        if self.dificultad is dificultad.Dificultad.dificil:
            if tablero == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']:
                posicionIngresada = random.choice([0, 2, 4, 6, 8])
                tableroNuevo = tablero[:posicionIngresada] + [self.letra] + tablero[posicionIngresada:]
            else:
                if self.arbol is None:
                    self.arbol = arbol_decisiones.ArbolDecisiones()
                    self.arbol.generarArbol(self.letra, tablero)
                self.arbol.cambiarRaizA(tablero)
                self.arbol.minimax()
                tableroNuevo = self.arbol.raiz.valor
        return tableroNuevo
