import time
import pyray
from raylib import colors

def main():
    width = 800
    height = 600
    pyray.init_window(width, height, "Game")
    ball = pyray.load_image("../../Downloads/basketball.png")
    ball_texture = pyray.load_texture_from_image(ball)
    pyray.unload_image(ball)
    ball_x = 100
    ball_y = 50
    i = 10
    j = 10
    while not pyray.window_should_close():
        if ball_x == (width - 100):
            i -= 20
        elif ball_x == 0:
            i += 20
        if ball_y == (height - 100):
            j -= 20
        elif ball_y == 0:
            j += 20
        time.sleep(0.1)
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        pyray.draw_texture(ball_texture, ball_x, ball_y, colors.WHITE)
        pyray.end_drawing()
        ball_x += i
        ball_y += j
    pyray.unload_texture(ball_texture)
    pyray.close_window()


if __name__ == '__main__':
    main()
