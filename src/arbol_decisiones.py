import math
class Nodo: # sirve como los posibles estados del tablero para el algoritmo minimax
    def __init__(self, valor):
        self.valor = valor # tablero = [0,1,2,3,4,5,6,7,8]
        self.siguientes = None

class ArbolDecisiones:
    def __int__(self):
        self.raiz = None
        self.letraCPU = None

    def _determinarGanador(self, valor):
        for i in range(0,9,3):
            if valor[i] != ' ' and valor[i] is valor[i + 1] and valor[i] is valor[i + 2]:
                return valor[i]
        for i in range(0, 3):
            if valor[i] != ' ' and valor[i] is valor[i + 3] and valor[i] is valor[i + 6]:
                return valor[i]
        if valor[0] != ' ' and valor[0] is valor[4] and valor[0] is valor[8]:
            return valor[0]
        if valor[2] != ' ' and valor[2] is valor[4] and valor[2] is valor[6]:
            return valor[2]
        return False

    def generarArbol(self, letraCPU, valor):
        self.raiz = self._generarArbol(letraCPU, valor)
        self.letraCPU = letraCPU

    def _generarArbol(self, letraIngresada, valor):
        tempRaiz = Nodo(valor)

        if self._determinarGanador(valor) is not False:
            return tempRaiz

        siguienteValores = []

        for i in range(9):
            if tempRaiz.valor[i] == ' ':
                tempSiguienteValor = tempRaiz.valor[:i] + [letraIngresada] + tempRaiz.valor[i + 1:]
                if tempSiguienteValor in siguienteValores:
                    continue
                else:
                    siguienteValores.append(tempSiguienteValor)
                    if tempRaiz.siguientes is None: # en el primero de los casos generar siguientes si es que hay que generarlos
                        tempRaiz.siguientes = []
                    tempRaiz.siguientes.append(self._generarArbol('X' if letraIngresada == 'O' else 'O' ,tempSiguienteValor))
        return tempRaiz

    def minimax(self):
        nuevoValor = self._minimax(self.raiz, self.letraCPU)[1]
        self.cambiarRaizA(nuevoValor)

    def _minimax(self, tempRaiz, letra):
        if tempRaiz.siguientes is None:
            ganador = self._determinarGanador(tempRaiz.valor)
            if ganador is not False:
                contador = 1
                for c in tempRaiz.valor:
                    if c == ' ':
                        contador += 1
                return [1 * (contador) if ganador is self.letraCPU else -1 * (contador), tempRaiz.valor]
            return [0, tempRaiz.valor]
        mejor = [-math.inf if letra is self.letraCPU else math.inf, tempRaiz.valor]
        for posibleMovida in tempRaiz.siguientes:
            tempPuntaje = self._minimax(posibleMovida, 'O' if letra == 'X' else 'X')
            if letra is self.letraCPU:
                if tempPuntaje[0] > mejor[0]:
                    mejor[0] = tempPuntaje[0]
                    mejor[1] = posibleMovida.valor
            else:
                if tempPuntaje[0] < mejor[0]:
                    mejor[0] = tempPuntaje[0]
                    mejor[1] = posibleMovida.valor
        return mejor

    def cambiarRaizA(self, valor):
        self._cambiarRaizA(self.raiz, valor)

    def _cambiarRaizA(self, tempRaiz, valor):
        if tempRaiz.valor is valor:
            self.raiz = tempRaiz
            return True
        if tempRaiz is None:
            return False
        if tempRaiz.siguientes is not None:
            for posibleCambio in tempRaiz.siguientes:
                if self._cambiarRaizA(posibleCambio, valor):
                    return True
        return False