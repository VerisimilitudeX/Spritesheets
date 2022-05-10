import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)
image_sheet = tsk.ImageSheet("Puffin_Fly.png", 5, 6)
puffin = tsk.Sprite(image_sheet, 400, 400)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()
    puffin.draw()

    puffin.update(c.get_time())
    pygame.display.flip()
    c.tick(30)
