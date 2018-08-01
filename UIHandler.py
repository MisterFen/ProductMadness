import pygame
import Config, ScoreHandler
from Hitmark import Hitmark


hitmarks = []

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


def purge_hitmarks():
    for x in hitmarks:
        print(x.time_active, x.max_time_active)
        if x.time_active > x.max_time_active:
            hitmarks.remove(x)
