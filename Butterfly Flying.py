import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("OutdoorPlowedField.jpg", 0, 0)
butterfly = tsk.Sprite("Butterfly.png", 0, 300)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    butterfly.center_x += 0.18 * c.get_time()
    butterfly.center_y += -0.1 * c.get_time()

    background.draw()
    butterfly.draw()

    c.tick(30)
    pygame.display.flip()
