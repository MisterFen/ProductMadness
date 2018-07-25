white = (255, 255, 255)
black = (0, 0, 0)

background_colour = black


def set_background():
    global background_colour
    background_colour = white


def draw_background(display):
    display.fill(background_colour)