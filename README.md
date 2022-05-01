# Spritesheets
* To animate a sprite, you can quickly change the image
* If the image changes fast enough, it blends into motion to the eye
* This is the same technique used in flipbooks, TV, and movies
# Frame
* In sprite animation, each single image is a frame
# Sprite Sheet
* A sprite sheet is a way of storing a whole animation in a single image
* A sprite sheet is a giant image with all the frames of an animation put together
* To create an animation, we will provide an image grid or "spritesheet"
* A sprite sheet is an image that looks like this
* We will use these to create a Python "ImageSheet" object that a sprite can use instead of an image filename
* To create an ImageSheet, we'll also have to specify how many rows and columns are in the grid of pictures
* Instead of loading an image file, a Sprite can load a tsk.ImageSheet
* A tsk.ImageSheet automatically cuts up a sprite sheet into individual frames
* When making an ImageSheet, you specify the number of rows and columns of frames in the sheet
* After loading the ImageSheet into the Sprite, you can use the Sprite like normal
# Update
* The .update() function tells a sprite to change its animation frame
* .update() is similar to .draw(), and should be called once every frame
* .update() needs to know how much time has passed in order to make the animation play at the right speed
# How to use a sprite sheet in PyGame
* Requires tsk library, since PyGame doesn't have sprite sheets built in
* sheet = tsk.ImageSheet(filename, rows, columns) makes an ImageSheet object * As in a Sprite, filename is a string for the sprite sheet's image file * rows and columns * are the size of the sprite sheet's dimensions
* ImageSheet automatically divides the sprite sheet into frames * Divides into the number of rows and columns you specified
* Sprites can use an ImageSheet as their image instead of a filename * Example: sprite = tsk.Sprite(sheet, x, y)
* The same ImageSheet can be used as the image for multiple Sprites
# How to make a sprite sheet animate
* sprite.animate(c.get_time()) must be called once per frame
* sprite is a Sprite object loaded with an ImageSheet
* c is a PyGame Clock object, created with pygame.time.Clock()
* The animation will automatically loop when it runs out of frames
# Why is it important to have a Clock?
* Programs should run at a consistent frame rate
* Consistent FPS makes a program's animation stay consistent on different computer speeds
* Calling clock.tick(30) every frame makes the program run at 30 FPS
* sprite.animate() needs a time argument so it can keep a consistent speed
* For the same reason, whenever you move a sprite, multiply the speed by clock.get_time()
* In these examples, clock is a pygame.time.Clock() object
# How to set the speed of an animation
* Animation rate: how fast the animation plays, in frames per second
* By default, Sprites with ImageSheets animate at 30 FPS * The image will change 30 times every second
* sprite.image_animation_rate stores a tsk.Sprite object's animation rate
* .image_animation_rate can get or set the animation rate
* The higher the animation rate, the faster the image will animate
* A rate of 0 will make the animation pause
* A negative rate will throw a runtime error
