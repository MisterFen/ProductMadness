import pygame


class Object:
    img = pygame.image.load('art/default.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))


class Table(Object):
    img = pygame.image.load('art/table.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 150
