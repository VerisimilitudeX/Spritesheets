import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("OpenMeadow.jpg", 0, 0)
sleep = tsk.ImageSheet("HedgehogSleep.png", 5, 6)
run = tsk.ImageSheet("HedgehogRun.png", 5, 6)

hedgehog = tsk.Sprite(run, 300, 200)

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Switching")

            if hedgehog.image == run:
                hedgehog.image = sleep
            elif hedgehog.image == sleep:
                hedgehog.image = run

    hedgehog.update(c.get_time())
    background.draw()
    hedgehog.draw()

    pygame.display.flip()
    c.tick(30)
