import sys, pygame, jugador, dificultad

if __name__ == '__main__':
    # pygame.init()
    # size = width, height = 728,728
    # speed = [1, 1]
    # bg_no_escalado = pygame.image.load("../resources/background.png")
    # bg = pygame.transform.scale(bg_no_escalado, (728,728))
    # white = 255, 255, 255
    #
    # screen = pygame.display.set_mode(size)
    #
    # ball = pygame.image.load("../resources/O.png")
    # ballrect = ball.get_rect()
    #
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT: sys.exit()
    #
    #     ballrect = ballrect.move(speed)
    #     if ballrect.left < 0 or ballrect.right > width:
    #         speed[0] = -speed[0]
    #     if ballrect.top < 0 or ballrect.bottom > height:
    #         speed[1] = -speed[1]
    #
    #     screen.fill(white)
    #     screen.blit(bg, (0,0))
    #     screen.blit(ball, ballrect)
    #     pygame.display.flip()


    def determinarGanador(valor):
        for i in range(0,9,3):
            if valor[i] is not ' ' and valor[i] is valor[i + 1] and valor[i] is valor[i + 2]:
                return True
        for i in range(0, 3):
            if valor[i] is not ' ' and valor[i] is valor[i + 3] and valor[i] is valor[i + 6]:
                return True
        if valor[0] is not ' ' and valor[0] is valor[4] and valor[0] is valor[8]:
            return True
        if valor[2] is not ' ' and valor[2] is valor[4] and valor[2] is valor[6]:
            return True
        return False

    tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    CPUfacil = jugador.JugadorCPU('facil', 'X', dificultad.Dificultad.facil)
    CPUdificil = jugador.JugadorCPU('dificil', 'O', dificultad.Dificultad.dificil)

    for i in range(9):
        print(tablero[0], ' | ', tablero[1], ' | ', tablero[2])
        print('-----------')
        print(tablero[3], ' | ', tablero[4], ' | ', tablero[5])
        print('-----------')
        print(tablero[6], ' | ', tablero[7], ' | ', tablero[8])
        print(" ")

        tablero = CPUfacil.movida(tablero)
        if (determinarGanador(tablero)):
            break
        tablero = CPUdificil.movida(tablero)
        if (determinarGanador(tablero)):
            break

    print(tablero[0], ' | ', tablero[1], ' | ', tablero[2])
    print('-----------')
    print(tablero[3], ' | ', tablero[4], ' | ', tablero[5])
    print('-----------')
    print(tablero[6], ' | ', tablero[7], ' | ', tablero[8])