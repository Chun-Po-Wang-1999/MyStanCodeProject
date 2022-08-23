"""
File: fire.py
Name: Louis
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    if the red part of a single pixel is significant, this pixel will turn into red(255)
    if not, then turn into gray
    """
    fire_img = SimpleImage(filename)
    for pixel in fire_img:
        avg = (pixel.red+pixel.blue+pixel.green) // 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return fire_img


def main():
    """
    distinguish the picture of before and after
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
