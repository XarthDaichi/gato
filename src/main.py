import sys, pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 728,728
    speed = [1, 1]
    bg_no_escalado = pygame.image.load("../resources/background.png")
    bg = pygame.transform.scale(bg_no_escalado, (728,728))

    screen = pygame.display.set_mode(size)

    ball = pygame.image.load("../resources/O.png")
    ballrect = ball.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(255,255,255)
        screen.blit(bg, (0,0))
        screen.blit(ball, ballrect)
        pygame.display.flip()
