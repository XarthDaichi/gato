import random
import queue
import jugador
from gui import dibujador as dib
from src import dificultad


class Juego:
    """
    Esta clase de encarga de mantener la funcionalidad del juego, el comienzo, turnos y demas

    Atributos
    ---------
    jugador1:Jugador
        Es el objeto tipo Jugador ya sea para CPU o humano

    jugador2:Jugador
        Es el objeto tipo Jugador ya sea para CPU o humano

    tablero:list
        Es el tablero del juego

    turnos:Queue
        Es donde se almacenan los jugadores para asignarle los turnos

    dibujador:Dibujador
        Es el encargado de generar la interfaz grafica

    Metodos
    -------
    comenzar(jugador1, jugador2)
        Se encarga de inicializar el juego

    turno()
        Se encarga de mantener la cola de turnos y ademas utiliza el metodo _determinarGanador() para determinar
        el ganador del juego, devolviendolo como un objeto

    terminarJuego(ganador)
        Se encarga de terminar el juego si el objeto ganador es nulo y si no lo es imprime el nombre del jugador
        ganador

    _determinarGanador()
        Determina si exite un ganador, si no existe returna False, si existe deveulve la letra (X o O) del ganador

    _tableroTieneVacios()
        Verifica si el tablero de juego tiene algun espacio vacio
    """

    def __init__(self, jugador1: jugador.Jugador, jugador2: jugador.Jugador):
        self.jugador1: jugador.Jugador = jugador1
        self.jugador2: jugador.Jugador = jugador2
        self.tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.turnos = queue.Queue()
        self.dibujador = dib.Dibujador()

    def comenzar(self, dibujador):
        """
        Se encarga de inicializar el juego

        Parametros
        ----------
        dibujador:Dibujador
            Es el objeto encargado de manejar la interfaz gafica
        """
        self.dibujador = dibujador
        if random.randint(1, 2) == 1:
            self.jugador1.letra = 'X'
            self.jugador2.letra = 'O'
            self.turnos.put(self.jugador1)
            self.turnos.put(self.jugador2)
        else:
            self.jugador1.letra = 'O'
            self.jugador2.letra = 'X'
            self.turnos.put(self.jugador2)
            self.turnos.put(self.jugador1)
        print('comenzando:')
        print(self.tablero[0], ' | ', self.tablero[1], ' | ', self.tablero[2])
        print('--------------------')
        print(self.tablero[3], ' | ', self.tablero[4], ' | ', self.tablero[5])
        print('--------------------')
        print(self.tablero[6], ' | ', self.tablero[7], ' | ', self.tablero[8])
        print(" ")
        self.dibujador.Juego()
        self.turno()

    def turno(self):
        """
        Se encarga de mantener la cola de turnos y ademas utiliza el metodo _determinarGanador() para determinar
        el ganador del juego, devolviendolo como un objeto
        """
        jugadorDeTurno = self.turnos.get()
        print('Turno de: ', jugadorDeTurno.nombre, '(', jugadorDeTurno.letra, ')')
        if type(jugadorDeTurno) == jugador.JugadorHumano:
            while True:
                nuevoTablero = jugadorDeTurno.movida(self.tablero, self.dibujador.getPosicion())
                if nuevoTablero is True:
                    break
        else:
            self.tablero = jugadorDeTurno.movida(self.tablero)

        self.dibujador.dibujaLetra(self.tablero)
        print(self.tablero[0], ' | ', self.tablero[1], ' | ', self.tablero[2])
        print('--------------------')
        print(self.tablero[3], ' | ', self.tablero[4], ' | ', self.tablero[5])
        print('--------------------')
        print(self.tablero[6], ' | ', self.tablero[7], ' | ', self.tablero[8])
        print("\n\n\n")

        nextJugador = self.turnos.get()
        if (type(jugadorDeTurno) == jugador.JugadorCPU) or (type(jugadorDeTurno) != jugador.JugadorCPU and nextJugador.getDificultad() != dificultad.Dificultad.imposible):
            if not self._determinarGanador() and self._tableroTieneVacios():
                self.turnos.put(nextJugador)
                self.turnos.put(jugadorDeTurno)
                self.turno()
            elif not self._tableroTieneVacios():
                if not self._determinarGanador():
                    self.terminarJuego(None)
                else:
                    self.terminarJuego(jugadorDeTurno)
            else:
                self.terminarJuego(jugadorDeTurno)
        else:
            self.turnos.put(nextJugador)
            self.turnos.put(jugadorDeTurno)
            self.turno()

    def terminarJuego(self, ganador):
        """
        Se encarga de terminar el juego si el objeto ganador es nulo y si no lo es imprime el nombre del jugador
        ganador

        Parametros
        ----------
        ganador:Jugador
            Se recibe dentro del metodo turno si existe o no un jugador ganador
        """
        while not self.turnos.empty():
            self.turnos.get()
        jugador.JugadorCPU.contadorParaNormal = 0
        self.dibujador.terminaJuego(ganador)
        if ganador is not None:
            print('Gana ', ganador.nombre, '(', ganador.letra, ')!!!!!')
        else:
            print('Empate!!!!')

    def _determinarGanador(self):
        """
        Determina si exite un ganador, si no existe returna False, si existe deveulve la letra (X o O) del ganador
        """
        for i in range(0, 9, 3):
            if self.tablero[i] != ' ' and self.tablero[i] is self.tablero[i + 1] and self.tablero[i] is self.tablero[
                i + 2]:
                return True
        for i in range(0, 3):
            if self.tablero[i] != ' ' and self.tablero[i] is self.tablero[i + 3] and self.tablero[i] is self.tablero[
                i + 6]:
                return True
        if self.tablero[0] != ' ' and self.tablero[0] is self.tablero[4] and self.tablero[0] is self.tablero[8]:
            return True
        if self.tablero[2] != ' ' and self.tablero[2] is self.tablero[4] and self.tablero[2] is self.tablero[6]:
            return True
        return False

    def _tableroTieneVacios(self):
        """
        Verifica si el tablero de juego tiene algun espacio vacio
        """
        for i in range(9):
            if self.tablero[i] == ' ':
                return True
        return False
