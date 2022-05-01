"""
LESSON: 5.2 - Spritesheet Animation
TECHNIQUE 4: Changing Frame Rates
DEMO 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)
image_sheet = tsk.ImageSheet("RoundShipSpin.png", 5, 3)
ship = tsk.Sprite(image_sheet, 400, 200)

timer = 0
speed_time = 1000
ship.image_animation_rate = 0


drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    timer += c.get_time()
    if timer > speed_time:
        ship.image_animation_rate += 2
        timer = 0


    background.draw()
    ship.draw()
    ship.update(c.get_time())

    pygame.display.flip()
    c.tick(30)