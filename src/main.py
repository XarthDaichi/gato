import jugador, dificultad, dibujador, pygame, sys, juego
if __name__ == '__main__':

    # pantalla = dibujador.Dibujador()

    # tablero = ['O', 'X', 'X', 'X', 'O', 'O', ' ', 'X', ' ']

    CPUfacil = jugador.JugadorCPU('CPU facil', ' ', dificultad.Dificultad.facil)
    CPUdificil = jugador.JugadorCPU('CPU dificil', ' ', dificultad.Dificultad.dificil)

    intanciaDeJuego = juego.Juego(CPUfacil, CPUdificil)