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

        self.screen = pygame.display.set_mode(size)
        O_no_escalado = pygame.image.load("../resources/O.png")
        X_no_escalado = pygame.image.load("../resources/X.png")
        self.O = pygame.transform.scale(O_no_escalado, (238, 238))
        self.X = pygame.transform.scale(X_no_escalado, (238, 238))

        self.iniciarMenu()

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

    # def draw_rect_alpha(self, surface, color, rect):
    #     shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    #     pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    #     surface.blit(shape_surf, rect)

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
        if posicionTablero % 3 == 0:
            coordx = -7
        elif posicionTablero % 3 == 1:
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
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        pygame.display.flip()

        # light shade of the button
        color_light = (215, 155, 98, 238)

        # dark shade of the button
        color_dark = (150, 108, 68, 238)

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
                    if botonPvP - 70 <= mouse[0] <= botonPvP + 70 and botonQuitheight - 20 <= mouse[1] <= botonQuitheight + 20:
                        pygame.quit()

                    if botonJugarwidth - 70 <= mouse[0] <= botonJugarwidth + 70 and botonJugarheight - 20 <= mouse[1] <= botonJugarheight + 20:
                        self.seleccionDeJuego()

            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            botonQuitRect = pygame.Rect(width / 2, height / 2, 140, 40)
            botonQuitRect.center = (width / 2, height / 2 + 80)
            botonPvP, botonQuitheight = width / 2, height / 2 + 80

            botonJugarRect = pygame.Rect(width / 2, height / 2, 140, 40)
            botonJugarRect.center = (width / 2, height / 2)
            botonJugarwidth, botonJugarheight = width / 2, height / 2

            rectParaVerTitulo = pygame.Rect(width / 2, height / 2, 500, 150)
            rectParaVerTitulo.center = (width / 2, height / 2 - 230)
            # codigo original (boton de quit)
            # if mouse is hovered on a button it
            # changes to lighter shade
            if botonPvP - 70 <= mouse[0] <= botonPvP + 70 and botonQuitheight - 20 <= mouse[1] <= botonQuitheight + 20:
                pygame.draw.rect(self.screen, color_light, botonQuitRect)
            else:
                pygame.draw.rect(self.screen, color_dark, botonQuitRect)

            if botonJugarwidth - 70 <= mouse[0] <= botonJugarwidth + 70 and botonJugarheight - 20 <= mouse[1] <= botonJugarheight + 20:
                pygame.draw.rect(self.screen, color_light, botonJugarRect)
            else:
                pygame.draw.rect(self.screen, color_dark, botonJugarRect)
            titulo1 = self.dibujaTexto('Operacion', width / 2, height / 2 - 260, 60)
            titulo2 = self.dibujaTexto('Gatito', width / 2, height / 2 - 200, 60)
            jugar = self.dibujaTexto('jugar', width / 2, height / 2, 20)
            quit = self.dibujaTexto('salir', width / 2, height / 2 + 80, 20)
            # superimposing the text onto our button
            self.screen.blit(jugar[0], jugar[1])
            self.screen.blit(quit[0], quit[1])
            pygame.draw.rect(self.screen, color_dark, rectParaVerTitulo)
            self.screen.blit(titulo1[0], titulo1[1])
            self.screen.blit(titulo2[0], titulo2[1])
            # updates the frames of the game
            pygame.display.update()

    def seleccionDeJuego(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg, (0, 0))
        pygame.display.flip()

        # light shade of the button
        color_light = (215, 155, 98, 238)

        # dark shade of the button
        color_dark = (150, 108, 68, 238)

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
                    if botonPvPwidth - 70 <= mouse[0] <= botonPvPwidth + 70 and botonPvPheight - 20 <= mouse[1] <= botonPvPheight + 20:
                        pass

                    if botonJvCPUwidth - 70 <= mouse[0] <= botonJvCPUwidth + 70 and botonJvCPUheight - 20 <= mouse[1] <= botonJvCPUheight + 20:
                        pass

                    if botonvolverwidth - 70 <= mouse[0] <= botonvolverwidth + 70 and botonvolverheight - 20 <= mouse[1] <= botonvolverheight + 20:
                        self.iniciarMenu()


            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            botonPvP = pygame.Rect(width / 2, height / 2, 140, 40)
            botonPvP.center = (width / 2, height / 2)
            botonPvPwidth, botonPvPheight = width / 2, height / 2

            botonJvCPU = pygame.Rect(width / 2, height / 2, 140, 40)
            botonJvCPU.center = (width / 2, height / 2 + 80)
            botonJvCPUwidth, botonJvCPUheight = width / 2, height / 2 + 80

            botonvolver = pygame.Rect(width / 2, height / 2, 140, 40)
            botonvolver.center = (width / 2, height / 2 + 160)
            botonvolverwidth, botonvolverheight = width / 2, height / 2 + 160

            rectParaVerTitulo = pygame.Rect(width / 2, height / 2, 500, 150)
            rectParaVerTitulo.center = (width / 2, height / 2 - 230)
            # codigo original (boton de quit)
            # if mouse is hovered on a button it
            # changes to lighter shade
            if botonPvPwidth - 70 <= mouse[0] <= botonPvPwidth + 70 and botonQuitheight - 20 <= mouse[1] <= botonQuitheight + 20:
                pygame.draw.rect(self.screen, color_light, botonPvP)
            else:
                pygame.draw.rect(self.screen, color_dark, botonPvP)

            if botonJvCPUwidth - 70 <= mouse[0] <= botonJvCPUwidth + 70 and botonJvCPUheight - 20 <= mouse[1] <= botonJvCPUheight + 20:
                pygame.draw.rect(self.screen, color_light, botonJvCPU)
            else:
                pygame.draw.rect(self.screen, color_dark, botonJvCPU)

            if botonvolverwidth - 70 <= mouse[0] <= botonvolverwidth + 70 and botonvolverheight - 20 <= mouse[1] <= botonvolverheight + 20:
                pygame.draw.rect(self.screen, color_light, botonvolver)
            else:
                pygame.draw.rect(self.screen, color_dark, botonvolver)
            titulo1 = self.dibujaTexto('Seleccion', width / 2, height / 2 - 260, 60)
            titulo2 = self.dibujaTexto('De Modo', width / 2, height / 2 - 200, 60)
            pvp = self.dibujaTexto('pvp', width / 2, height / 2, 20)
            jvcpu = self.dibujaTexto('J v CPU', width / 2, height / 2 + 80, 20)
            volver = self.dibujaTexto('volver', width / 2, height / 2 + 160, 20)
            # superimposing the text onto our button
            self.screen.blit(pvp[0], pvp[1])
            self.screen.blit(jvcpu[0], jvcpu[1])
            self.screen.blit(volver[0], volver[1])
            pygame.draw.rect(self.screen, color_dark, rectParaVerTitulo)
            self.screen.blit(titulo1[0], titulo1[1])
            self.screen.blit(titulo2[0], titulo2[1])
            # updates the frames of the game
            pygame.display.update()