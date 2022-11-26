import pygame
import sys


class Dibujador:
    """
    Es la clase encargada de generar la interfaz grafica y se implementa usando la libreria PyGame

    Metodos
    -------
    dibujaText(string, coordx, coordy, fontSize)
        Determina el titulo, posicion y tamaño para presentar en la interfaz

    dibujaLetra(letra, posicionTablero)
        Se encarga de dibujar la letra del jugador, X o O en el tablero

    iniciarMenu()
        Presenta el menu en la interfaz con sus diferentes opciones
    """

    def __init__(self):
        pygame.init()
        size = width, height = 728, 728
        bg_no_escalado = pygame.image.load("../resources/backgroundMenu.png")
        self.bg = pygame.transform.scale(bg_no_escalado, (728, 728))
        white = 255, 255, 255

        self.screen = pygame.display.set_mode(size)
        O_no_escalado = pygame.image.load("../resources/O.png")
        X_no_escalado = pygame.image.load("../resources/X.png")
        self.O = pygame.transform.scale(O_no_escalado, (238, 238))
        self.X = pygame.transform.scale(X_no_escalado, (238, 238))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

            self.screen.fill(white)
            self.screen.blit(self.bg, (0, 0))
            self.iniciarMenu()
            pygame.display.flip()

    def dibujaTexto(self, string, coordx, coordy, fontSize):  # Function to set text
        """
        Determina el titulo, posicion y tamaño para presentar en la interfaz

        Parametros
        ----------
        string:str
            Es el titulo a presentar
        coordx:int
            Determina la posicion en eje X del string
        coordy:int
            Determina la posicion en eje Y del string
        fontSize:int
            Determina el tamaño de la fuente del string
        """
        font = pygame.font.Font('../resources/ka1.ttf', fontSize)
        # (0, 0, 0) is black, to make black text
        text = font.render(string, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (coordx, coordy)
        return (text, textRect)

    def dibujaLetra(self, letra, posicionTablero):
        """
        Se encarga de dibujar la letra del jugador, X o O en el tablero

        Parametros
        ----------
        letra:str
            Es la letra, X o O, para presentar en la interfaz
        posicionTablero:int
            Es donde se vaya a dibujar la letra de acuerdo con coordenadas del tablero
        """
        letraDibujar = self.O if letra == 'O' else self.X
        if posicionTablero <= 2:
            coordy = -7
        elif posicionTablero <= 5:
            coordy = 254
        else:
            coordy = 497
        if posicionTablero % 3 is 0:
            coordx = -7
        elif posicionTablero % 3 is 1:
            coordx = 254
        else:
            coordx = 497
        self.screen.blit(letraDibujar, (coordx, coordy))
        pygame.display.update()

    # def testWriteSomething(self): example to use the setText function
    #     pygame.init()
    #     window = pygame.display.set_mode((728, 728))
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT: sys.exit()
    #         window.fill((255, 255, 255))  # Fills the whole window with white
    #         # Places "Text in Pygame!" with an x,y coord of 250, 250 and 60 font size
    #         totalText = set_text("Text in Pygame!", 350, 250, 60)
    #         window.blit(totalText[0], totalText[1])
    #         pygame.display.update()

    def iniciarMenu(self):
        """
        Presenta el menu en la interfaz con sus diferentes opciones
        """
        # light shade of the button
        color_light = (170, 170, 170)

        # dark shade of the button
        color_dark = (100, 100, 100)

        # stores the width of the
        # screen into a variable
        width = self.screen.get_width()

        # stores the height of the
        # screen into a variable
        height = self.screen.get_height()

        while True:

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()

                # checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button the game is terminated
                    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                        pygame.quit()

            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            # if mouse is hovered on a button it
            # changes to lighter shade
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.draw.rect(self.screen, color_light, [width / 2, height / 2, 140, 40])

            else:
                pygame.draw.rect(self.screen, color_dark, [width / 2, height / 2, 140, 40])

            text = self.dibujaTexto('quit', width / 2 + 70, height / 2 + 20, 20)
            # superimposing the text onto our button
            self.screen.blit(text[0], text[1])

            # updates the frames of the game
            pygame.display.update()
