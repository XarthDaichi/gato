import dificultad

class Jugador:
    def __int__(self, nombre, letra):
        self.nombre = nombre
        self.letra = letra

    def movida(self):
        pass

class JugadorHumano(Jugador):
    def __init__(self, nombre, letra):
        super().__init__(nombre, letra)

    def movida(self):
        pass

class JugadorCPU(Jugador):
    def __init__(self, letra, dificultad):
        super().__init__('CPU', letra)
        self.dificultad = dificultad

    def movida(self):
        pass