"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Coder side, creates one class with some default constant and methods
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.brick_cols = brick_cols
        self.brick_rows = brick_rows
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball_origin_x = window_width/2-ball_radius
        self.ball_origin_y = window_height/2-ball_radius
        self.ball.filled = True
        self.window.add(self.ball)

        # create a score board
        self.score = 0
        self.score_label = GLabel(f"Score: {self.score}")
        self.score_label.font = '-20'
        self.window.add(self.score_label, x=0, y=self.window.height)

        # a gate to judge if the ball is moving
        self.ball_is_moving = False
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.click)
        onmousemoved(self.paddle_move)

        self.brick_count = 0
        # Draw rainbow bricks
        self.color_red = ['IndianRed', 'LightCoral', 'Salmon', 'DarkSalmon', 'LightSalmon']
        self.color_orange = ['DarkOrange', 'OrangeRed', 'Tomato', 'Coral', 'LightSalmon']
        self.color_yellow = ['LemonChiffon', 'Yellow', 'Khaki', 'PaleGoldenrod', 'LightYellow']
        self.color_green = ['LimeGreen', 'Lime', 'LawnGreen', 'Chartreuse', 'GreenYellow']
        self.color_blue = ['DodgerBlue', 'DeepSkyBlue', 'SkyBlue', 'LightSkyBlue', 'PowderBlue']
        self.color_purple = ['Magenta', 'Fuchsia', 'Orchid', 'Violet', 'Plum']
        # randomly choose a color set
        self.color_set = [self.color_red, self.color_orange, self.color_yellow, self.color_green, self.color_blue, self.color_purple]
        self.choose_color_set = random.choice(self.color_set)

        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=j*(brick_spacing+brick_width), y=brick_offset+i*(brick_spacing+brick_height))
                brick.filled = True
                #  the bricks are divided into 5 groups
                if i < brick_rows//5:  # group 1
                    brick.fill_color = self.choose_color_set[0]
                elif brick_rows // 5 <= i < brick_rows*2 // 5:  # group 2
                    brick.fill_color = self.choose_color_set[1]
                elif brick_rows*2 // 5 <= i < brick_rows * 3 // 5:  # group 3
                    brick.fill_color = self.choose_color_set[2]
                elif brick_rows * 3 // 5 <= i < brick_rows * 4 // 5:  # group 4
                    brick.fill_color = self.choose_color_set[3]
                else:  # group 5
                    brick.fill_color = self.choose_color_set[4]
                self.brick_count += 1  # calculate how many bricks
                self.window.add(brick)

        self.ball_radius = ball_radius
        #  the four corner of ball need checked
        # self.maybe_object_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        # self.maybe_object_2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
        #                                                 self.ball.y)
        # self.maybe_object_3 = self.window.get_object_at(self.ball.x,
        #                                                 self.ball.y + 2 * self.ball_radius)
        # self.maybe_object_4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
        #                                                 self.ball.y + 2 * self.ball_radius)
    # a method to change the ball velocity to zero

    def ball_stop(self):
        self.__dx = 0
        self.__dy = 0

    # check if ball hits the paddle
    # def check_paddle_collision(self):
    #     self.maybe_object_1 = self.window.get_object_at(self.ball.x, self.ball.y)
    #     self.maybe_object_2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
    #                                                     self.ball.y)
    #     self.maybe_object_3 = self.window.get_object_at(self.ball.x,
    #                                                     self.ball.y + 2 * self.ball_radius)
    #     self.maybe_object_4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
    #                                                     self.ball.y + 2 * self.ball_radius)
    #
    #     if self.maybe_object_3 is self.paddle or self.maybe_object_4 is self.paddle:
    #         self.y_collision()

    # check if ball hits the brick, it will return the object of brick ; if not, return None
    def check_collision(self):
        self.maybe_object_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.maybe_object_2 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
                                                        self.ball.y)
        self.maybe_object_3 = self.window.get_object_at(self.ball.x,
                                                        self.ball.y + 2 * self.ball_radius)
        self.maybe_object_4 = self.window.get_object_at(self.ball.x + 2 * self.ball_radius,
                                                        self.ball.y + 2 * self.ball_radius)
        if self.maybe_object_1 is not None and self.maybe_object_1 and self.maybe_object_1 is not self.score_label:
            return self.maybe_object_1
        elif self.maybe_object_2 is not None and self.maybe_object_2 and self.maybe_object_2 is not self.score_label:
            return self.maybe_object_2
        elif self.maybe_object_3 is not None and self.maybe_object_3 and self.maybe_object_3 is not self.score_label:
            return self.maybe_object_3
        elif self.maybe_object_4 is not None and self.maybe_object_4 and self.maybe_object_4 is not self.score_label:
            return self.maybe_object_4
        else:
            return None

    #  the paddle will follow the mouse position on x-axis and the mouse's position locates at the center of paddle
    def paddle_move(self, mouse):
        if mouse.x < self.paddle.width / 2:  # if the mouse exceeds left side window:
            self.paddle.x = 0
        elif mouse.x > self.window.width - self.paddle.width/2:  # if the mouse exceeds right side window:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    #  the whole program activates by one mouse click
    def click(self, event):
        if not self.ball_is_moving:
            self.set_ball_velocity()  # the ball get a velocity
            self.ball_is_moving = True  # if this method turns to 'True', the mouse click would be malfunctioned

    # the ball get a random velocity
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:  # the odd of velocity is same for two sides
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    # getter
    def get_dx(self):
        return self.__dx

    # getter
    def get_dy(self):
        return self.__dy

    # change x-dir velocity
    def x_collision(self):
        self.__dx = -self.__dx

    # change y-dir velocity
    def y_collision(self):
        self.__dy = - self.__dy


