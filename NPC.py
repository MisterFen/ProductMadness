import pygame

class NPC:
    img = pygame.image.load('art/default.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))


class Dev(NPC):

    img = pygame.image.load('art/dev1.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 38
        self.height = 38
        self.state = "working"
        self.time_working = 0
        self.rotate_speed = 0
        self.angle = 90
        self.img_rect = self.img.get_rect()

    def on_tick(self):
        if self.state == "working":
            self.time_working += 1
        if self.state == "spinning":
            self.rotate()

    def draw(self, display):
        display.blit(self.img,(self.x, self.y))

    def rotate(self):
        self.img = pygame.transform.rotate(self.img, self.angle)