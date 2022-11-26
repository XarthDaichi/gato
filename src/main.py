import jugador, dificultad, dibujador, pygame, sys
if __name__ == '__main__':

    # pantalla = dibujador.Dibujador()

    def determinarGanador(valor):
        for i in range(0,9,3):
            if valor[i] != ' ' and valor[i] is valor[i + 1] and valor[i] is valor[i + 2]:
                print('gana ', valor[i], '!!!!!')
                return True
        for i in range(0, 3):
            if valor[i] != ' ' and valor[i] is valor[i + 3] and valor[i] is valor[i + 6]:
                print('gana ', valor[i], '!!!!!')
                return True
        if valor[0] != ' ' and valor[0] is valor[4] and valor[0] is valor[8]:
            print('gana ', valor[0], '!!!!!')
            return True
        if valor[2] != ' ' and valor[2] is valor[4] and valor[2] is valor[6]:
            print('gana ', valor[2], '!!!!!')
            return True
        return False

    # tablero = ['O', 'X', 'X', 'X', 'O', 'O', ' ', 'X', ' ']
    tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print('starting:')
    print(tablero[0], ' | ', tablero[1], ' | ', tablero[2])
    print('--------------------')
    print(tablero[3], ' | ', tablero[4], ' | ', tablero[5])
    print('--------------------')
    print(tablero[6], ' | ', tablero[7], ' | ', tablero[8])
    print(" ")

    CPUfacil = jugador.JugadorCPU('facil', 'X', dificultad.Dificultad.facil)
    CPUdificil = jugador.JugadorCPU('dificil', 'O', dificultad.Dificultad.dificil)

    for i in range(9):
        tablero = CPUdificil.movida(tablero)
        print(CPUdificil.nombre, ':')
        print(tablero[0], ' | ', tablero[1], ' | ', tablero[2])
        print('--------------------')
        print(tablero[3], ' | ', tablero[4], ' | ', tablero[5])
        print('--------------------')
        print(tablero[6], ' | ', tablero[7], ' | ', tablero[8])
        print(" ")
        if (determinarGanador(tablero)):
            break

        print('\n\n\n================================================================================')

        tablero = CPUfacil.movida(tablero)
        print(CPUfacil.nombre, ':')
        print(tablero[0], ' | ', tablero[1], ' | ', tablero[2])
        print('--------------------')
        print(tablero[3], ' | ', tablero[4], ' | ', tablero[5])
        print('--------------------')
        print(tablero[6], ' | ', tablero[7], ' | ', tablero[8])
        print(" ")
        if (determinarGanador(tablero)):
            break

        print('\n\n\n================================================================================')