# -*- encoding: utf-8 -*-

from pynput.mouse import Listener
from pyscreeze import pixel


def on_click(x, y, button, pressed):
    if button.name == 'left' and pressed:
        print(f'position: ({x}, {y})')
        print_color(get_screen_color(x, y), '\t')
    elif button.name == 'middle':
        return False


def get_screen_color(x, y):
    pix = pixel(x, y)
    return pix[:3]


def print_color(color, start='', end=''):
    hex_color = '#'
    for c in color:
        hex_color += format(c, "x") if c > 15 else f'0{format(c, "x")}'
    print(f'{start}color(10): {color}{end}')
    print(f'{start}color(16): {hex_color}{end}')


def get_color():
    try:
        print(f'Click the left mouse button to pick color or click the middle of the mouse to exit.')
        with Listener(on_click=on_click) as listener:
            listener.join()
    except Except:
        print('ERROR!!!')


def main():
    get_color()
    