"""
LESSON: 5.2 - Spritesheet Animation
TECHNIQUE 3: Switching Animations
PRACTICE 1
"""
import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Space.jpg", 0, 0)

yellow = tsk.ImageSheet("RoundShipSpin.png", 5, 3)
purple = tsk.ImageSheet("RoundShipPurpleSpin.png", 5, 3)

ship = tsk.Sprite(yellow, 500, 100)
is_purple = False
purple_timer = 2000

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_purple = True
            print("Switching to purple!")
            ship.image = purple

    if is_purple:
        purple_timer -= c.get_time()
        if purple_timer <= 0:
            purple_timer = 2000
            is_purple = False
            print("Switching back to yellow!")
            ship.image = yellow

    x, y = pygame.mouse.get_pos()
    ship.center = x, y

    background.draw()
    ship.draw()
    ship.update(c.get_time())

    pygame.display.flip()
    c.tick(30)


# Turn in your Coding Exercise.
