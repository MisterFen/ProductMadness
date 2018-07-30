import pygame
import random
import ScoreHandler


class NPC:
    img = pygame.image.load('art/default.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))


class Dev(NPC):

    img = pygame.image.load('art/dev1.png')
    random.seed()

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 38
        self.height = 38
        self.state = "working"
        self.time_working = 0
        self.time_working_limit = random.randint(10, 1000)
        self.time_since_rotated = 0
        self.rotate_increment = 90
        self.angle = 90
        self.img_rect = self.img.get_rect()

    def on_tick(self):
        if self.state == "working":
            self.time_working += 1
            if self.time_working >= self.time_working_limit:
                self.state = "spinning"
        if self.state == "spinning":
            self.time_since_rotated += 1
            if self.time_since_rotated == self.rotate_increment:
                self.rotate()
                self.time_since_rotated = 0

    def draw(self, display):
        display.blit(self.img,(self.x, self.y))

    def rotate(self):
        self.img = pygame.transform.rotate(self.img, self.angle)

    def on_player_interact(self):
        ScoreHandler.increase_score(1)
        if self.state == "spinning":
            self.state = "working"
            ScoreHandler.increase_score(49)
        if self.state == "working":
            self.time_working = 0
