import time
import pyray
from raylib import colors

def main():
    width = 800
    height = 600
    pyray.init_window(width, height, "Platform")
    y = 550
    x = 0
    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(colors.BLACK)
        time.sleep(0.1)
        if pyray.is_key_down(pyray.KeyboardKey.KEY_A) and x >= 20:
            x -= 20
        if pyray.is_key_down(pyray.KeyboardKey.KEY_D) and x <= (width - 220):
            x += 20
        pyray.draw_rectangle(x, y, 200, 10, colors.RED)
        pyray.end_drawing()
    pyray.close_window()


if __name__ == '__main__':
    main()
