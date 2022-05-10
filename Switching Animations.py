import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("OutdoorLake.jpg", 0, 0)

walking = tsk.ImageSheet("Puffin_Walk.png", 5, 6)
swimming = tsk.ImageSheet("Puffin_Swim.png", 5, 6)

puffin = tsk.Sprite(walking, 400, 100)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if puffin.image == walking:
                print("Switching to swimming!")
                puffin.image = swimming
            else:
                print("Switching to walking.")
                puffin.image = walking

    puffin.center_y += 0.03 * c.get_time()

    background.draw()
    puffin.draw()
    puffin.update(c.get_time())

    pygame.display.flip()
    c.tick(30)    
