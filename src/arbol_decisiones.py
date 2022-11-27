import math


class Nodo:
    """
    Esta clase sirve como los posibles estados del tablero

    Atributos
    ---------
    tablero:list
        Es la letra, X o O, asignada a cada espacio del tablero
    
    siguientes:Nodo
        Los siguientes nodos del arbol
    """

    def __init__(self, tablero):
        self.tablero = tablero  # tablero = [0,1,2,3,4,5,6,7,8]
        self.siguientes = None


class ArbolDecisiones:
    """
    Esta clase crea el arbol de decisiones para los jugadores CPU

    Atributos
    ---------
    raiz:nodo
        Un nodo con valor X o O dependiendo del arbol a generar

    letraCPU:str
        Es la letra asignada al CPU, sea X o O

    Metodos
    -------
    _determinarGanador(tablero)
        Determina si exite un ganador, si no existe returna False, si existe deveulve la letra (X o O) del ganador

    generarArbol(letraCPU, tablero)
        Es el wrapper del metodo _generarArbol

    _generarArbol(letraIngresada, tablero)
        Genera arbol de decisiones tomando en cuenta el resultado de funcion _determinarGanador y un tablero dado

    minimax()
        Es el wrapper del metodo _minimax

    minimaxSiempreGane()
        Una implementacion del minimax donde siempre gana CPU

    minimaxImposible()
        Una implementacion del minimax donde el comportamiento del CPU es... especial...

    _minimax(tempRaiz, letra)
        Este metodo es donde se aplica la logica del algoritmo minimax para minimizar la perdida maxima al realizar
        un movimiento

    cambiarRaizA(tablero)
        Es el wrapper del metodo _cambiarRaizA

    _cambiarRaizA(tempRaiz, tablero)
        Es un metodo para cambiar la raiz del arbol para no generar el arbol desde cero

    cambiarRaizAImposible(tablero)
        Es el wrapper del metodo _cambiarRaizAImposible

    _cambiarRaizAImposible(tempRaiz, tablero)
        Una variacion del metodo cambiarRaizA()

    """

    def __int__(self):
        self.raiz = None
        self.letraCPU = None

    def _determinarGanador(self, tablero):
        """
        Determina si exite un ganador, si no existe returna False, si existe deveulve la letra (X o O) del ganador

        Parametros
        ----------
        tablero:list
            El tablero del juego

        Retorna
        -------
        tablero[i]
            Retorna tablero[i] cuando se tiene la primera linea llena o columna llena

        tablero[0]
            Retorna tablero[0] si este es igual a tablero[4] y tablero[8], haciendo una diagonal

        tablero[2]
            Retorna tablero [2] si este es igual a tablero[4] y tablero[6], haciendo una diagonal

        False
            Retorna False si ninguna de las condiciones anteriores se cumple
        """
        for i in range(0, 9, 3):
            if tablero[i] != ' ' and tablero[i] == tablero[i + 1] and tablero[i] == tablero[i + 2]:
                return tablero[i]
        for i in range(0, 3):
            if tablero[i] != ' ' and tablero[i] == tablero[i + 3] and tablero[i] == tablero[i + 6]:
                return tablero[i]
        if tablero[0] != ' ' and tablero[0] == tablero[4] and tablero[0] == tablero[8]:
            return tablero[0]
        if tablero[2] != ' ' and tablero[2] == tablero[4] and tablero[2] == tablero[6]:
            return tablero[2]
        return False

    def generarArbol(self, letraCPU, tablero):
        """
        Es el wrapper del metodo _generarArbol
        """
        self.raiz = self._generarArbol(letraCPU, tablero)
        self.letraCPU = letraCPU

    def _generarArbol(self, letraIngresada, tablero):
        """
        Genera arbol de decisiones tomando en cuenta el resultado de funcion _determinarGanador y un tablero dado

        Parametros
        ----------
        letraIngresada:str
            Es la letra que se ingresa por parte del jugador

        tablero:list
            El tablero del juego
        """
        tempRaiz = Nodo(tablero)

        if self._determinarGanador(tablero) is not False:
            return tempRaiz

        siguienteValores = []

        for i in range(9):
            if tempRaiz.tablero[i] == ' ':
                tempSiguienteValor = tempRaiz.tablero[:i] + [letraIngresada] + tempRaiz.tablero[i + 1:]
                if tempSiguienteValor in siguienteValores:
                    continue
                else:
                    siguienteValores.append(tempSiguienteValor)
                    if tempRaiz.siguientes is None:  # en el primero de los casos generar siguientes si es que hay que generarlos
                        tempRaiz.siguientes = []
                    tempRaiz.siguientes.append(
                        self._generarArbol('X' if letraIngresada == 'O' else 'O', tempSiguienteValor))
        return tempRaiz

    def minimax(self):
        """
        Es el wrapper del metodo _minimax
        """
        nuevoValor = self._minimax(self.raiz, self.letraCPU)[1]
        self.cambiarRaizA(nuevoValor)
        return nuevoValor

    def minimaxSiempreGane(self):
        """
        Una implementacion del minimax donde siempre gana CPU
        """
        nuevoValor = self._minimax(self.raiz, 'X' if self.letraCPU == 'O' else 'O')[1]
        self.cambiarRaizA(nuevoValor)

    def minimaxImposible(self):
        """
        Una implementacion del minimax donde el comportamiento del CPU es... especial...
        """
        nuevoValor = self._minimax(self.raiz, self.letraCPU)[1]
        self.cambiarRaizAImposible(nuevoValor)

    def _minimax(self, tempRaiz, letra):
        """
        Este metodo es donde se aplica la logica del algoritmo minimax para minimizar la perdida maxima al realizar
        un movimiento

        Parametros
        ----------
        tempRaiz:nodo
            Es el nodo del tablero del arbol en que se encuentre la iteracion del minimax

        letra:str
            Es la letra asignada al CPU, X o O

        Retorna
        -------
        [1 * (contador) if ganador == self.letraCPU else -1 * (contador), tempRaiz.tablero]
            Si existe ganador, si el ganador es CPU devuelve tablero positivo, si no tablero negativo

        [0, tempRaiz.tablero]
            Si no existe ganador

        mejor
            Si no se cumple ninguna de las condiciones anteriores, es la mejor movida posible
        """
        if tempRaiz.siguientes is None:
            ganador = self._determinarGanador(tempRaiz.tablero)
            if ganador is not False:
                contador = 1
                for c in tempRaiz.tablero:
                    if c == ' ':
                        contador += 1
                return [1 * (contador) if ganador == self.letraCPU else -1 * (contador), tempRaiz.tablero]
            return [0, tempRaiz.tablero]
        mejor = [-math.inf if letra == self.letraCPU else math.inf, tempRaiz.tablero]
        for posibleMovida in tempRaiz.siguientes:
            tempPuntaje = self._minimax(posibleMovida, 'O' if letra == 'X' else 'X')
            if letra == self.letraCPU:
                if tempPuntaje[0] > mejor[0]:
                    mejor[0] = tempPuntaje[0]
                    mejor[1] = posibleMovida.tablero
            else:
                if tempPuntaje[0] < mejor[0]:
                    mejor[0] = tempPuntaje[0]
                    mejor[1] = posibleMovida.tablero
        return mejor

    def cambiarRaizA(self, tablero):
        """
        Es el wrapper del metodo _cambiarRaizA
        """
        self.raiz = self._cambiarRaizA(tablero)

    def _cambiarRaizA(self, tablero):
        """
        Es un metodo para cambiar la raiz del arbol para no generar el arbol desde cero

        Parametro
        ---------
        tablero:list
            El tablero del juego
        """
        if self.raiz.tablero == tablero:
            return self.raiz
        if self.raiz.siguientes is not None:
            for posibleCambio in self.raiz.siguientes:
                if posibleCambio.tablero == tablero:
                    return posibleCambio

    def cambiarRaizAImposible(self, tablero):
        """
        Es el wrapper del metodo _cambiarRaizAImposible
        """
        self._cambiarRaizAImposible(self.raiz, tablero)

    def _cambiarRaizAImposible(self, tempRaiz, tablero):
        """
        Una variacion del metodo cambiarRaizA()
        """
        if tempRaiz.tablero is tablero:
            self.raiz = tempRaiz
            return True
        if tempRaiz is None:
            return False
        if tempRaiz.siguientes is not None:
            for posibleCambio in tempRaiz.siguientes:
                if self._cambiarRaizAImposible(posibleCambio, tablero):
                    return True
        return False
