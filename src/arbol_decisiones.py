import math
# TODO documentacion incompleta, terminar


class Nodo:
    """
    Esta clase sirve como los posibles estados del tablero para el algoritmo minimax

    Atributos
    ---------
    valor:list

    siguientes:Nodo
    """ # sirve como los posibles estados del tablero para el algoritmo minimax
    def __init__(self, valor):
        """
        Parametros
        ----------
        valor:

        """
        self.valor = valor  # tablero = [0,1,2,3,4,5,6,7,8]
        self.siguientes = None


class ArbolDecisiones:
    """
    Esta clase crea el arbol de decisiones para los juegadores CPU

    Atributos
    ---------
    raiz:nodo
    letraCPU:str

    Metodos
    -------
    _determinarGanador(valor)
        Determina si exite un ganador, si no existe returna False, si existe deveulve la letra (X o O) del ganador

    generarArbol(letraCPU, valor)
        Es el wrapper del metodo _generarArbol

    _generarArbol(letraIngresada, valor)
        Genera arbol de decisiones tomando en cuenta el resultado de funcion _determinarGanador y un tablero dado

    minimax()
        Es el wrapper del metodo _minimax

    _minimax(tempRaiz, letra)
        Lorem Ipsum

    cambiarRaizA(valor)
        Es el wrapper del metodo _cambiarRaizA

    _cambiarRaizA(tempRaiz, valor)
        Lorem Ipsum

    cambiarRaizAImposible(valor)
        Es el wrapper del metodo _cambiarRaizAImposible

    _cambiarRaizAImposible(tempRaiz, valor)
        Lorem Ipsum

    """

    def __int__(self):
        self.raiz = None
        self.letraCPU = None

    def _determinarGanador(self, valor):
        """
        Determina si exite un ganador, si no existe returna False, si existe deveulve la letra (X o O) del ganador

        Parametros
        ----------
        valor:str

        Retorna
        -------
        valor[i]
            Retorna valor[i] cuando ...

        valor[0]
            Retorna valor[0] si este es igual a valor[4] y valor[8], haciendo una diagonal

        valor[2]
            Retorna valor [2] si este es igual a valor[4] y valor[6], haciendo una diagonal

        False
            Retorna False si ninguna de las condiciones anteriores se cumple
        """
        for i in range(0, 9, 3):
            if valor[i] != ' ' and valor[i] == valor[i + 1] and valor[i] == valor[i + 2]:
                return valor[i]
        for i in range(0, 3):
            if valor[i] != ' ' and valor[i] == valor[i + 3] and valor[i] == valor[i + 6]:
                return valor[i]
        if valor[0] != ' ' and valor[0] == valor[4] and valor[0] == valor[8]:
            return valor[0]
        if valor[2] != ' ' and valor[2] == valor[4] and valor[2] == valor[6]:
            return valor[2]
        return False

    def generarArbol(self, letraCPU, valor):
        """
        Es el wrapper del metodo _generarArbol
        """
        self.raiz = self._generarArbol(letraCPU, valor)
        self.letraCPU = letraCPU

    def _generarArbol(self, letraIngresada, valor):
        """
        Genera arbol de decisiones tomando en cuenta el resultado de funcion _determinarGanador y un tablero dado

        Parametros
        ----------
        letraIngresada:str
            Es la letra que se ingresa por parte del jugador

        valor:

        """
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
        """
        Es el wrapper del metodo _minimax
        """
        nuevoValor = self._minimax(self.raiz, self.letraCPU)[1]
        self.cambiarRaizA(nuevoValor)
        return nuevoValor

    def minimaxSiempreGane(self):
        nuevoValor = self._minimax(self.raiz, 'X' if self.letraCPU == 'O' else 'O')[1]
        self.cambiarRaizA(nuevoValor)

    def minimaxImposible(self):
        nuevoValor = self._minimax(self.raiz, self.letraCPU)[1]
        self.cambiarRaizAImposible(nuevoValor)

    def _minimax(self, tempRaiz, letra):
        """
        Este metodo es donde se aplica la logica del algoritmo minimax para determinar la jugada con mayor o menor
        posibilidad de ganar

        Parametros
        ----------
        tempRaiz:
            Lorem

        letra:str

        """
        if tempRaiz.siguientes is None:
            ganador = self._determinarGanador(tempRaiz.valor)
            if ganador is not False:
                contador = 1
                for c in tempRaiz.valor:
                    if c == ' ':
                        contador += 1
                return [1 * (contador) if ganador == self.letraCPU else -1 * (contador), tempRaiz.valor]
            return [0, tempRaiz.valor]
        mejor = [-math.inf if letra == self.letraCPU else math.inf, tempRaiz.valor]
        for posibleMovida in tempRaiz.siguientes:
            tempPuntaje = self._minimax(posibleMovida, 'O' if letra == 'X' else 'X')
            if letra == self.letraCPU:
                if tempPuntaje[0] > mejor[0]:
                    mejor[0] = tempPuntaje[0]
                    mejor[1] = posibleMovida.valor
            else:
                if tempPuntaje[0] < mejor[0]:
                    mejor[0] = tempPuntaje[0]
                    mejor[1] = posibleMovida.valor
        return mejor

    def cambiarRaizA(self, valor):
        """Es el wrapper del metodo _cambiarRaizA"""
        self.raiz = self._cambiarRaizA(valor)

    def _cambiarRaizA(self, valor):
        """Lorem Ipsum"""
        if self.raiz.siguientes is not None:
            for posibleCambio in self.raiz.siguientes:
                if posibleCambio.valor == valor:
                    return posibleCambio

    def cambiarRaizAImposible(self, valor):
        """Es el wrapper del metodo _cambiarRaizAImposible"""
        self._cambiarRaizA(self.raiz, valor)

    def _cambiarRaizAImposible(self, tempRaiz, valor):
        """Lorem Ipsum"""
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
