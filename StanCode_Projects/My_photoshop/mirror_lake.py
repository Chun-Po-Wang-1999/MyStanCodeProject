"""
File: mirror_lake.py
Name: Louis
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    create a new blank background, so we can use the origin picture to reflect by y = 0 to the blank background.
    """
    reflect_img = SimpleImage(filename)
    b_img = SimpleImage.blank(reflect_img.width, reflect_img.height*2)

    for x in range(reflect_img.width):
        for y in range(reflect_img.height):
            img_p = reflect_img.get_pixel(x, y)
            b_img_1 = b_img.get_pixel(x, y)

            b_img_1.red = img_p.red
            b_img_1.green = img_p.green
            b_img_1.blue = img_p.blue

            b_img_2 = b_img.get_pixel(x, b_img.height-1-y)
            b_img_2.red = img_p.red
            b_img_2.green = img_p.green
            b_img_2.blue = img_p.blue
    return b_img


def main():
    """
    distinguish the picture of before and after.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
