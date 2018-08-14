import pygame


class Hitmark:

    def __init__(self, x, y, msg):
        self.x = x
        self.y = y
        self.msg = msg
        self.font_size = 12
        self.move_speed = 0.1
        self.time_active = 0
        self.max_time_active = 85
        self.my_font = pygame.font.SysFont('Verdana', self.font_size)
        self.text_surface = self.my_font.render(str(msg), False, (0, 0, 0))
        pygame.font.init()

    def draw(self, display):
        display.blit(self.text_surface, (self.x, self.y))
        self.y -= self.move_speed
        self.time_active += 1


class ImageHitmark(Hitmark):
    img = pygame.image.load('art/default.png')

    def __init__(self, val, x, y):
        self.x = x
        self.y = y
        self.move_speed = 0.1
        self.time_active = 0
        self.max_time_active = 85
        if val == "extend deadline":
            self.img = pygame.image.load('art/deadline_ability_hitmark.png')

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))
        self.y -= self.move_speed
        self.time_active += 1

    def get_image(self):
        return self.img