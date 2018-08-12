import pygame


class InteractionIcon:

    def __init__(self, pos):
        self.pos = pos
        self.img = pygame.image.load('art/interaction_icon.png')
        self.time_active = 0

    def get_image(self):
        return self.img

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def on_tick(self):
        self.time_active += 1