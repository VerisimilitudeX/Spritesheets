import pygame
import tsk
pygame.init()

window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SchoolHallway.jpg", 0, 0)
robot = tsk.Sprite("Robot.png", 100, 200)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    robot.center_x += 0.1 * c.get_time()
    
    background.draw()
    robot.draw()

    pygame.display.flip()
    c.tick(30)
