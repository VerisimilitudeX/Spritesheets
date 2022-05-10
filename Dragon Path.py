#### ---- SET UP ---- ####

# --- Libraries --- #
import pygame
import tsk
pygame.init()

# --- Program variables --- #
window = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# --- Sprites --- #
background = tsk.Sprite("FantasyPlains.jpg", 0, 0)

wizardimagesheet = tsk.ImageSheet("WizardWalking.png", 4, 6)
dragonimagesheet = tsk.ImageSheet("DragonFlying.png", 4, 6)
wizard = tsk.Sprite(wizardimagesheet, 150, 280)
dragon = tsk.Sprite(dragonimagesheet, 650, 30)

wizard.image_animation_rate = 30

# --- Timing Variables --- #
dragon_appeared = False
dragon_current_state = 0
how_long_dragon_should_be_visible = 2000
how_long_dragon_should_be_invisible = 3000

#### ---- MAIN LOOP ---- ####
running = True
while running:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update timer --- #
    dragon_current_state += c.get_time()

    if dragon_appeared == True and dragon_current_state > how_long_dragon_should_be_visible:
        dragon_current_state = 0
        dragon_appeared = False

    if dragon_appeared == False and dragon_current_state > how_long_dragon_should_be_invisible:
        dragon_current_state = 0
        dragon_appeared = True

    # --- Move with arrow keys --- #

    if dragon_appeared == False:

        if tsk.get_key_pressed(pygame.K_RIGHT):
            wizard.center_x += 5
            wizard.flip_x = True

        if tsk.get_key_pressed(pygame.K_LEFT):
            wizard.center_x -= 5
            wizard.flip_x = True
            
    # --- Animate --- #
    if dragon_appeared == True:
        wizard.image_animation_speed = 0
    else:
        wizard.image_animation_speed = 30

    dragon.update(c.get_time())
    wizard.update(c.get_time())

    # ---  Draw --- #
    wizard.draw
    background.draw
    if dragon_appeared == True:
        dragon.draw

    pygame.display.flip()
    c.tick(30)
