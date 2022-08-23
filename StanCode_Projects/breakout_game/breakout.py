"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

user side, control the animation and turns of lives
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 100			# Number of attempts
POINT_PER_BRICK = 10

def main():
    graphics = BreakoutGraphics()
    attempt = 0
    while True:
        pause(FRAME_RATE)
        ball_speed_x = graphics.get_dx()
        ball_speed_y = graphics.get_dy()
        # ball speed would go faster if user hits more bricks
        if graphics.brick_count < graphics.brick_cols*graphics.brick_rows*2/3:
            ball_speed_x *= 1.1
            ball_speed_y *= 1.1
        if graphics.brick_count < graphics.brick_cols * graphics.brick_rows / 3:
            ball_speed_x *= 1.2
            ball_speed_y *= 1.2
        graphics.ball.move(ball_speed_x, ball_speed_y)
        if attempt == NUM_LIVES:  # die
            break
        if graphics.brick_count == 0:  # hit all bricks
            break
        # when the ball hits left or right side of window, it rebounds.
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.x_collision()
        # when the ball hits the top of window, it rebounds
        if graphics.ball.y < 0:
            graphics.y_collision()
        # the ball fall out of the bottom corner, meaning attempt plus one ,and the ball move back to the start point
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            graphics.ball.x = graphics.ball_origin_x
            graphics.ball.y = graphics.ball_origin_y
            graphics.ball_stop()  # the ball is at the restart condition
            graphics.ball_is_moving = False  # for next mouse click
            attempt += 1
        # check if the ball hit something
        if graphics.check_collision() is not None:
            if graphics.check_collision() is graphics.paddle:  # if the ball hits the paddle:
                graphics.y_collision()
                graphics.ball.y = graphics.paddle.y - graphics.ball.height
            else:  # if the ball hits a brick:
                graphics.y_collision()
                graphics.window.remove(graphics.check_collision())  # remove hit brick
                graphics.brick_count -= 1
                graphics.score += POINT_PER_BRICK  # get point of hitting a brick
                graphics.score_label.text = f"Score: {graphics.score}"


if __name__ == '__main__':
    main()
