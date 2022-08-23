"""
File: my_drawing.py
Name: Louis
----------------------
TODO: Using different shape to form a picture.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640


def main():
    """
    Title: Minion

    This is phythoned Minion.
    pythoned minion is Gru's favorite because he helps Gru analyze every vicious mission with python
    so they could steal the moon.

    """
    window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT, title='Minion')
    background = GRect(WINDOW_WIDTH, WINDOW_HEIGHT)
    background.filled = True
    background.fill_color = 'gold'
    window.add(background)

    left_eye_1 = GOval(160, 160, x=85, y=120)
    left_eye_1.filled = True
    left_eye_1.fill_color = 'silver'
    left_eye_1.color = 'silver'
    window.add(left_eye_1)

    right_eye_1 = GOval(160, 160, x=235, y=120)
    right_eye_1.filled = True
    right_eye_1.fill_color = 'silver'
    right_eye_1.color = 'silver'
    window.add(right_eye_1)

    left_eye_2 = GOval(130, 130, x=100, y=135)
    left_eye_2.filled = True
    left_eye_2.fill_color = 'gold'
    left_eye_2.color = 'silver'
    window.add(left_eye_2)

    right_eye_2 = GOval(130, 130, x=250, y=135)
    right_eye_2.filled = True
    right_eye_2.fill_color = 'gold'
    right_eye_2.color = 'silver'
    window.add(right_eye_2)

    left_white_of_eye = GArc(130, 110, 0, 359.9, x=100, y=145)
    left_white_of_eye.filled = True
    left_white_of_eye.fill_color = 'snow'
    left_white_of_eye.color = 'snow'
    window.add(left_white_of_eye)

    right_white_of_eye = GArc(130, 110, 0, 359.9, x=250, y=145)
    right_white_of_eye.filled = True
    right_white_of_eye.fill_color = 'snow'
    right_white_of_eye.color = 'snow'
    window.add(right_white_of_eye)

    left_eyeball = GOval(50, 50, x=145, y=180)
    left_eyeball.filled = True
    left_eyeball.fill_color = 'sienna'
    left_eyeball.color = 'maroon'
    window.add(left_eyeball)

    right_eyeball = GOval(50, 50, x=280, y=180)
    right_eyeball.filled = True
    right_eyeball.fill_color = 'sienna'
    right_eyeball.color = 'maroon'
    window.add(right_eyeball)

    left_eyeball_1 = GOval(20, 20, x=160, y=195)
    left_eyeball_1.filled = True
    left_eyeball_1.fill_color = '#1C2833'
    left_eyeball_1.color = '#1C2833'
    window.add(left_eyeball_1)

    right_eyeball_1 = GOval(20, 20, x=295, y=195)
    right_eyeball_1.filled = True
    right_eyeball_1.fill_color = '#1C2833'
    right_eyeball_1.color = '#1C2833'
    window.add(right_eyeball_1)

    left_buckle = GPolygon()
    left_buckle.add_vertex((0, 190))
    left_buckle.add_vertex((87, 180))
    left_buckle.add_vertex((90, 230))
    left_buckle.add_vertex((0, 235))
    left_buckle.filled = True
    left_buckle.fill_color = 'dimgray'
    left_buckle.color = 'dimgray'
    window.add(left_buckle)

    left_buckle_1 = GPolygon()
    left_buckle_1.add_vertex((0, 210))
    left_buckle_1.add_vertex((86, 205))
    left_buckle_1.add_vertex((89, 210))
    left_buckle_1.add_vertex((0, 215))
    left_buckle_1.filled = True
    left_buckle_1.fill_color = '#424949'
    left_buckle_1.color = '#424949'
    window.add(left_buckle_1)

    right_buckle = GPolygon()
    right_buckle.add_vertex((WINDOW_WIDTH, 190))
    right_buckle.add_vertex((393, 180))
    right_buckle.add_vertex((390, 230))
    right_buckle.add_vertex((WINDOW_WIDTH, 235))
    right_buckle.filled = True
    right_buckle.fill_color = 'dimgray'
    right_buckle.color = 'dimgray'
    window.add(right_buckle)

    right_buckle_1 = GPolygon()
    right_buckle_1.add_vertex((WINDOW_WIDTH, 210))
    right_buckle_1.add_vertex((393, 205))
    right_buckle_1.add_vertex((390, 210))
    right_buckle_1.add_vertex((WINDOW_WIDTH, 215))
    right_buckle_1.filled = True
    right_buckle_1.fill_color = '#424949'
    right_buckle_1.color = '#424949'
    window.add(right_buckle_1)

    smile = GArc(220, 180, 190, 160, x=135, y=300)
    smile.color = '#1C2833'
    window.add(smile)

    paint = GRect(window.width, 420, x=0, y=430)
    paint.filled = True
    paint.fill_color = '#212F3C'
    paint.color = '#212F3C'
    window.add(paint)

    paint_1 = GRect(window.width, 15, x=0, y=415)
    paint_1.filled = True
    paint_1.fill_color = '#283747'
    paint_1.color = '#283747'
    window.add(paint_1)

    label = GLabel('M i n i o n ', x=95, y=550)
    label.font = 'Helvetica-48-bold'
    label.color = '#E67E22'
    window.add(label)

    label_1 = GLabel('def', x=15, y=35)
    label_1.font = 'Helvetica-18'
    label_1.color = '#F39C12'
    window.add(label_1)

    label_2 = GLabel(' main', x=50, y=35)
    label_2.font = 'Helvetica-18'
    label_2.color = '#FCF3CF'
    window.add(label_2)

    label_3 = GLabel(' ():', x=105, y=32)
    label_3.font = 'Helvetica-16'
    label_3.color = 'snow'
    window.add(label_3)
if __name__ == '__main__':
    main()
