import pygame
import ScoreHandler

class Object:
    img = pygame.image.load('art/default.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.time_active = 0

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

    def on_tick(self):
        self.time_active += 1


class Table(Object):
    img = pygame.image.load('art/table.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 150
        self.time_active = 0


class Computer(Object):
    img = pygame.image.load('art/computer.png')
    answer_buzz_score = 300

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 28
        self.height = 36
        self.state = "idle"
        self.locked_state = False
        self.idle_time = 0
        self.lock_timer = 500

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))

    def on_tick(self):
        if self.state == "idle":
            self.idle_time += 1
        if self.idle_time >= self.lock_timer:
            if not self.locked_state:
                self.lock()

    def on_player_interact(self):
        if self.locked_state:
            self.unlock()
        else:
            if self.state == "idle":
                self.boop()
            if self.state == "buzzing":
                self.answer_buzz()

    def boop(self):
        self.idle_time = 0

    def unlock(self):
        self.state = "idle"
        self.locked_state = False
        self.idle_time = 0

    def answer_buzz(self):
        self.state = "idle"
        self.idle_time = 0
        ScoreHandler.increase_score(self.answer_buzz_score)

    def lock(self):
        self.locked_state = True
        self.state = "locked"
