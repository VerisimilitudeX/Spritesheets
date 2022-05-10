#### ---- SET UP ---- ####

# --- Libraries ---  #
import tsk
import pygame
pygame.init()

# --- Animation variables --- #
window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("HedgehogHouse.jpg", 0, 0)

sleep_sheet = tsk.ImageSheet("HedgehogSleep.png", 5, 6)

brush_sheet = tsk.ImageSheet("HedgehogBrush.png", 5, 6)

run_sheet = tsk.ImageSheet("HedgehogRun.png", 5, 6)

hedgehog = tsk.Sprite(sleep_sheet, 100, 100)

# --- Loop variables --- #
drawing = True

#### ---- MAIN LOOP ---- ####
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # --- Mouse input --- #
    x, y = pygame.mouse.get_pos()
    hedgehog.center = x, y

    # --- Change animation --- #
    if hedgehog.x < 200:
        if hedgehog.image is not sleep_sheet:
            hedgehog.image = sleep_sheet
            
    elif hedgehog.x < 550:
        if hedgehog.image is not brush_sheet:
            hedgehog.image = brush_sheet

    else:
        if hedgehog.image is not run_sheet:
            hedgehog.image = run_sheet


    # --- Animate and draw --- ###
    hedgehog.update(c.get_time())
    background.draw()
    hedgehog.draw()
    pygame.display.flip()

    c.tick(30)
