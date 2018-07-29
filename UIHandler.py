import pygame
import Config, ScoreHandler


def draw(display):
    draw_score(display)


def draw_score(display):
    font_size = 30
    pygame.font.init()
    my_font = pygame.font.SysFont('Verdana', font_size)
    text_surface = my_font.render('Score: ' + str(ScoreHandler.score), False, (0, 0, 0))
    display.blit(text_surface, (10, Config.display_height - font_size - 10))
