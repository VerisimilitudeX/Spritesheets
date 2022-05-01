"""
LESSON: 5.2 - Spritesheet Animation
TECHNIQUE 3: Switch Animations
PRACTICE 2
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("OutdoorHills.jpg", 0, 0)

sleep = tsk.ImageSheet("HedgehogSleep.png", 5, 6)
run = tsk.ImageSheet("HedgehogRun.png", 5, 6)

hedgehog = tsk.Sprite(sleep, 170, 170)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Switching to run!")
            hedgehog.image = run
        elif event.type == pygame.MOUSEBUTTONUP:
            print("Switching to sleep!")
            hedgehog.image = sleep

    background.draw()
    hedgehog.draw()
    hedgehog.update(c.get_time())

    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
