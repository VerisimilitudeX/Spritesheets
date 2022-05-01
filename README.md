# Spritesheets
* To animate a sprite, you can quickly change the image
* If the image changes fast enough, it blends into motion to the eye
* This is the same technique used in flipbooks, TV, and movies
# Frame:
* In sprite animation, each single image is a frame
# Sprite Sheet:
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
# Update:
* The .update() function tells a sprite to change its animation frame
* .update() is similar to .draw(), and should be called once every frame
* .update() needs to know how much time has passed in order to make the animation play at the right speed
