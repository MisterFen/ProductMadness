import Config
import pygame


class Player:
    img = pygame.image.load('art/player.png')

    def __init__(self):
        self.x = Config.player_start_x
        self.y = Config.player_start_y
        self.speed = 5

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
