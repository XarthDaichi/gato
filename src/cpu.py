from enum import Enum

class Dificultad(Enum):
    facil = 1
    normal = 2
    dificil = 3

class CPU:
    def __int__(self):
        self.dificultad = None
