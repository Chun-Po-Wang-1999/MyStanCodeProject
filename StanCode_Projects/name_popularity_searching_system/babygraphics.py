"""
File: babygraphics.py
Name: Louis
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + ((width - (GRAPH_MARGIN_SIZE * 2)) / len(YEARS)) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT, get_x_coordinate(CANVAS_WIDTH, i), 0)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color = 0
    for ls in lookup_names:
        if color == 3:
            color = 0
        for i in range(11):
            year1 = 1900 + 10 * i
            year_index1 = i
            if str(year1) in name_data[ls]:
                rank1 = name_data[ls][str(year1)]
                # y1-position
                plot1 = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000*int(rank1)
            else:
                rank1 = '*'
                plot1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

            year2 = str(1900 + 10 * (i + 1))
            year_index2 = i + 1
            if str(year2) in name_data[ls]:
                rank2 = name_data[ls][str(year2)]
                # y2-position
                plot2 = GRAPH_MARGIN_SIZE+(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000*int(rank2)
            else:
                rank2 = '*'
                plot2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index1), plot1,
                               get_x_coordinate(CANVAS_WIDTH, year_index2), plot2, width=LINE_WIDTH, fill=COLORS[color])
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index1) + TEXT_DX, plot1, text=(str(ls)+' '+str(rank1)),
                               anchor=tkinter.SW, font='times 10')
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, year_index2) + TEXT_DX, plot2, text=(str(ls)+' '+str(rank2)),
                               anchor=tkinter.SW, font='times 10')
        color += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
