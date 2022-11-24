class Nodo: # sirve como los posibles estados del tablero para el algoritmo minimax
    def __init__(self, valor):
        self.valor = valor # tablero = [0,1,2,3,4,5,6,7,8]
        self.siguientes = None

class ArbolDecisiones:
    def __int__(self):
        self.root = None

    def insertar(self, valor):
        if self.root is None:
            self.root = Nodo(valor)
            return

