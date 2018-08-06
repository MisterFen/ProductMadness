import pygame
import Config, ScoreHandler
from Hitmark import Hitmark
from Button import Button


hitmarks = []

button1 = Button(250, 500, 100, 50, "Play")
button2 = Button(450, 500, 100, 50, "Quit")

title_image = pygame.image.load('art/title_image.png')
title_image_x = 200
title_image_y = 50
title_images = [title_image]
title_buttons = [button1, button2]


def draw(display):
    draw_score(display)
    purge_hitmarks()
    draw_hitmarks(display)


def draw_score(display):
    font_size = 30
    pygame.font.init()
    my_font = pygame.font.SysFont('Verdana', font_size)
    text_surface = my_font.render('Score: ' + str(ScoreHandler.score), False, (0, 0, 0))
    display.blit(text_surface, (10, Config.display_height - font_size - 10))


def draw_hitmarks(display):
    for x in hitmarks:
        x.draw(display)


def create_hitmark(x, y, msg):
    hitmark = Hitmark(x, y, msg)
    hitmarks.append(hitmark)


def check_title_buttons_clicked():
    x, y = pygame.mouse.get_pos()
    for i in title_buttons:
        if x < i.rect.x + i.rect.width:
            if x > i.rect.x:
                if y < i.rect.y + i.rect.height:
                    if y > i.rect.y:
                        return i.text


def purge_hitmarks():
    for x in hitmarks:
        if x.time_active > x.max_time_active:
            hitmarks.remove(x)
            del x


def draw_title(display):
    display.fill((200, 200, 200))
    display.blit(title_image, (title_image_x, title_image_y))
    for x in title_buttons:
        x.draw(display)
