import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Hills.jpg", 0, 0)
hedgehog = tsk.Sprite("HedgehogRunPose.png", 100, 200)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    x, y = pygame.mouse.get_pos()
    hedgehog.center = (x, y)

    background.draw()
    hedgehog.draw()

    pygame.display.flip()
    c.tick(30)
