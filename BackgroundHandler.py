import pygame

white = (255, 255, 255)
black = (0, 0, 0)

background_colour = black
background_img = pygame.image.load('art/carpet.png')

def set_background():
    global background_colour
    background_colour = white


def draw_background(display):
    display.blit(background_img, (0, 0))
