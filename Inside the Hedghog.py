"""
LESSON: 5.2 - Spritesheet Animation
EXERCISE: Inside The Hedgehog
"""

#### ---- SET UP ---- ####

# --- Libraries ---  #

# Import the tsk library
import tsk

# Import the pygame library
import pygame

# Initialize pygame
pygame.init()

# --- Animation variables --- #

# Open a new window of size [1018, 573] and assign to
# window
window = pygame.display.set_mode([1018, 573])

# Create a new Clock
c = pygame.time.Clock()

# Create a SPRITE variable called background
# using the "HedgehogHouse.jpg" image at (0, 0)
background = tsk.Sprite("HedgehogHouse.jpg", 0, 0)

# Create a new IMAGESHEET object called sleep_sheet
# using the "HedgehogSleep.png" image with 5 rows
# and 6 columns.
sleep_sheet = tsk.ImageSheet("HedgehogSleep.png", 5, 6)

# Create a new IMAGESHEET object called brush_sheet
# using the "HedgehogBrush.png" image with 5 rows
# and 6 columns.
brush_sheet = tsk.ImageSheet("HedgehogBrush.png", 5, 6)

# Create a new IMAGESHEET object called run_sheet
# using the "HedgehogRun.png" image with 5 rows
# and 6 columns.
run_sheet = tsk.ImageSheet("HedgehogRun.png", 5, 6)

# Create a SPRITE variable called hedgehog using
# sleep_sheet as the image, positioned at (100, 100).
hedgehog = tsk.Sprite(sleep_sheet, 100, 100)

# --- Loop variables --- #

# Create a variable called drawing and assign it True
drawing = True

#### ---- MAIN LOOP ---- ####

# Loop while drawing
while drawing:

    # --- Event loop --- #

    # Create an event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # --- Mouse input --- #

    # Get the position of the mouse and store
    # it in the variables x, y
    x, y = pygame.mouse.get_pos()

    # Set the hedgehog's CENTER to x, y
    hedgehog.center = x, y

    # --- Change animation --- #

    # If the hedgehog's x is less than 340
    if hedgehog.x < 200:

        # If the hedgehog's IMAGE is not sleep_sheet
        if hedgehog.image is not sleep_sheet:

            # Set the hedgehog's IMAGE to sleep_sheet
            hedgehog.image = sleep_sheet

    # Elif the hedgehog's x is less than 680
    elif hedgehog.x < 550:

        # If the hedgehog's IMAGE is not brush_sheet
        if hedgehog.image is not brush_sheet:

           # Set IMAGE for the hedgehog to brush_sheet
            hedgehog.image = brush_sheet

    # Else
    else:

        # If the hedgehog's IMAGE is not run_sheet
        if hedgehog.image is not run_sheet:

            # Set IMAGE for the hedgehog to run_sheet
            # ---> TEST AFTER THIS LINE <--- #
            hedgehog.image = run_sheet


    # --- Animate and draw --- ###

    # UPDATE the hedgehog's animation with c.get_time()
    hedgehog.update(c.get_time())

    # DRAW the background
    background.draw()

    # DRAW the hedgehog
    hedgehog.draw()

    # Flip the display
    pygame.display.flip()

    # Tick c at 30 FPS
    # ---> TEST AFTER THIS LINE <--- #
    c.tick(30)

# Turn in your Coding Exercise.
