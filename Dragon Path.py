"""
LESSON: 5.2 - Spritesheet Animation
EXERCISE: Dragon Path
"""

#### ---- SET UP ---- ####

# --- Libraries --- #

# Import and set up pygame and tsk
import pygame
import tsk
pygame.init()

# --- Program variables --- #

# Open a window of size [1018, 573] and create a clock
window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# --- Sprites --- #

# Create a background sprite in the top-left using
# "FantasyPlains.jpg"
background = tsk.Sprite("FantasyPlains.jpg", 0, 0)

# Create two ImageSheets with "WizardWalking.png" and
# "DragonFlying.png", each with 4 rows and 6 columns,
# and use them to create two sprites at 150, 280
# (wizard) and 650, 30 (dragon)
# ---> TEST AFTER THESE LINES <--- #
wizardimagesheet = tsk.ImageSheet("WizardWalking.png", 4, 6)
dragonimagesheet = tsk.ImageSheet("DragonFlying.png", 4, 6)
wizard = tsk.Sprite(wizardimagesheet, 150, 280)
dragon = tsk.Sprite(dragonimagesheet, 650, 30)

# Set the wizard's animation rate to 30
wizard.image_animation_rate = 30

# --- Timing Variables --- #

# Create variables to track the following values:
# Whether the dragon has appeared (starts False), how
# long the dragon has been in its current state (0),
# how long the dragon should be visible (2000), and how
# long the dragon should be invisible (3000)
dragon_appeared = False
dragon_current_state = 0
how_long_dragon_should_be_visible = 2000
how_long_dragon_should_be_invisible = 3000

#### ---- MAIN LOOP ---- ####

# Create a main loop
running = True
while running:

    # --- Event loop --- #

    # Create an event loop
    # ---> TEST AFTER THIS LINE <--- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update timer --- #

    # Increment the dragon's current state timer by
    # get_time
    dragon_current_state += c.get_time()

    # If the dragon is appearing and the state timer
    # is greater than the visiblility time, set the
    # state timer to 0 and set the appearance boolean
    # to False
    if dragon_appeared == True and dragon_current_state > how_long_dragon_should_be_visible:
        dragon_current_state = 0
        dragon_appeared = False

    # If the dragon is not appearing and state timer
    # is greater than the invisibility time, set the
    # state timer to 0 and set the appearance boolean
    # to True
    # ---> TEST AFTER THIS LINE <--- #
    if dragon_appeared == False and dragon_current_state > how_long_dragon_should_be_invisible:
        dragon_current_state = 0
        dragon_appeared = True

    # --- Move with arrow keys --- #

    # If the dragon is not appearing
    if dragon_appeared == False:

        # If the right arrow key is down, move the
        # wizard right and face him to the right
        if tsk.get_key_pressed(pygame.K_RIGHT):
            wizard.center_x += 5
            wizard.flip_x = True

        # If the left arrow key is down, move the
        # wizard left and face him to the left
        # ---> TEST AFTER THIS LINE <--- #
        if tsk.get_key_pressed(pygame.K_LEFT):
            wizard.center_x -= 5
            wizard.flip_x = True
            
    # --- Animate --- #

    # If the dragon is appearing, pause the wizard's
    # animation rate, otherwise set it to 30
    if dragon_appeared == True:
        wizard.image_animation_speed = 0
    else:
        wizard.image_animation_speed = 30
                                                    
    # Update the dragon and wizard's animations
    dragon.update(c.get_time())
    wizard.update(c.get_time())

    # ---  Draw --- #

    # Draw the three sprites, but only draw the dragon
    # if it is currently appearing
    wizard.draw
    background.draw
    if dragon_appeared == True:
        dragon.draw

    # Flip the display and tick the clock at 30 frames
    # ---> TEST AFTER THIS LINE <--- #
    pygame.display.flip()
    c.tick(30)
#
# Turn in your Coding Exercise.
#