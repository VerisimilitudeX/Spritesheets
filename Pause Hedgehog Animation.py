import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("OutdoorBushes.jpg", 0, 0)
image_sheet = tsk.ImageSheet("HedgehogRun.png", 5, 6)
hedgehog = tsk.Sprite(image_sheet, 300, 250)
hedgehog.image_animation_rate = 30

timer = 0
speed_time = 1000

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Pausing or unpausing!")
            if hedgehog.image_animation_rate == 30:
                hedgehog.image_animation_rate = 0
            elif hedgehog.image_animation_rate == 0:
                hedgehog.image_animation_rate = 30

    background.draw()
    hedgehog.draw()
    hedgehog.update(c.get_time())

    c.tick(30)
    pygame.display.flip()


# Turn in your Coding Exercise.
