from enum import Enum


class Instruccion(Enum):
    """
    Es una clase enumeradora donde se asignan enteros para cada instruccion posible en la interfaz

    Enumeradores
    ------------
    quit = o
    seleccionDeModo = 1
    PvP = 2
    PvCPU = 3
    volver = 4
    """
    quit = 0
    seleccionDeModo = 1
    pvp = 2
    pvc = 3
    volver = 4
