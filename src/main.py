import jugador, dificultad, juego
from gui import dibujador
from gui import instruccion as inst


if __name__ == '__main__':

    gui = dibujador.Dibujador()

    while True:
        instruccion = gui.iniciarMenu()
        if instruccion is inst.Instruccion.seleccionDeModo:
            instruccion = gui.seleccionDeJuego()
            if instruccion is inst.Instruccion.pvp:
                jugador1 = jugador.JugadorHumano(gui.pedirNombre(), ' ')
                jugador2 = jugador.JugadorHumano(gui.pedirNombre(), ' ')
            elif instruccion is inst.Instruccion.pvc:
                jugador1 = jugador.JugadorHumano(gui.pedirNombre(), ' ')
                jugador2 = jugador.JugadorCPU(' ', gui.pedirDificultad())
            if instruccion is inst.Instruccion.volver:
                continue
            else:
                elJuego = juego.Juego(jugador1, jugador2)
                gui.Juego()
                elJuego.comenzar(gui)
        elif instruccion is inst.Instruccion.quit:
            break