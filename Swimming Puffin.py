import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("LakeSideView.jpg", 0, 0)

puffin_sheet = tsk.ImageSheet("PuffinSwim.png", 5, 6)
puffin = tsk. Sprite(puffin_sheet, 500, 400)


drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    background.draw()

    puffin.update(c.get_time())
    puffin.draw()

    pygame.display.flip()
    c.tick(30)
