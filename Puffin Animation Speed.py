import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)
image_sheet = tsk.ImageSheet("PuffinFly.png", 5, 6)
puffin = tsk.Sprite(image_sheet, 300, 100)
puffin.image_animation_rate = 30

timer = 0
slow_time = 80

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Speeding up!")
            puffin.image_animation_rate += 30

    timer += c.get_time()
    if timer > slow_time and puffin.image_animation_rate > 0:
        timer = 0
        puffin.image_animation_rate -= 1


    background.draw()
    puffin.draw()
    puffin.update(c.get_time())

    pygame.display.flip()
    c.tick(30)
