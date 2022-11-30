import jugador as player
import juego as game
import dificultad as dif
from gui import dibujador
from gui import instruccion as inst


if __name__ == '__main__':

    gui = dibujador.Dibujador()

    while True:
        instruccion = gui.iniciarMenu()
        if instruccion is inst.Instruccion.seleccionDeModo:
            instruccion = gui.seleccionDeJuego()
            if instruccion is inst.Instruccion.pvp:
                jugador1 = player.JugadorHumano(gui.pedirNombre(), ' ')
                jugador2 = player.JugadorHumano(gui.pedirNombre(), ' ')
            elif instruccion is inst.Instruccion.pvc:
                jugador1 = player.JugadorHumano(gui.pedirNombre(), ' ')
                jugador2 = player.JugadorCPU(' ', gui.pedirDificultad())
            if instruccion is inst.Instruccion.volver:
                continue
            else:
                elJuego = game.Juego(jugador1, jugador2)
                gui.Juego()
                elJuego.comenzar(gui)
        elif instruccion is inst.Instruccion.quit:
            break

    # testCPU1 = player.JugadorCPU('X', gui.pedirDificultad(), 'CPU Dificil')
    # testCPU2 = player.JugadorCPU('O', gui.pedirDificultad(), 'CPU Imposible')
    # testJuego = game.Juego(testCPU1, testCPU2)
    # testJuego.comenzar(gui)
