import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Stage.png", 0, 0)
pug = tsk.Sprite("PugBee.png", 900, 250)
pug.flip_x = True

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    pug.center_x += -0.2 * c.get_time()

    background.draw()
    pug.draw()

    c.tick(30)
    pygame.display.flip()
