import pygame
import ScoreHandler, UIHandler

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
    buzz_img = pygame.image.load('art/computer_buzz.png')
    answer_buzz_score = 300
    max_buzz_timer = 1500
    lock_timer = 500

    def __init__(self, x, y):
        self.x = self.start_x = x
        self.y = self.start_y = y
        self.width = 28
        self.height = 36
        self.state = "idle"
        self.locked_state = False
        self.idle_time = 0
        self.time_to_buzz = self.max_buzz_timer
        self.set_new_buzz_timer()

    def on_start(self):
        self.x = self.start_x
        self.y = self.start_y
        self.state = "idle"
        self.locked_state = False
        self.idle_time = 0
        self.time_to_buzz = self.max_buzz_timer
        self.set_new_buzz_timer()

    def draw(self, display):
        if self.locked_state:
            self.img = pygame.image.load('art/computer_locked.png')
        else:
            self.img = pygame.image.load('art/computer.png')
        display.blit(self.img, (self.x, self.y))

        if self.state == "buzzing":
            display.blit(self.buzz_img, (self.x, self.y))

    def on_tick(self):
        self.time_to_buzz -= 1
        if self.time_to_buzz <= 0:
            self.start_buzzing()
        if self.state == "idle":
            self.idle_time += 1
        if self.idle_time >= self.lock_timer:
            if not self.locked_state:
                self.lock()

    def on_player_interact(self):
        if self.locked_state:
            self.unlock()
            UIHandler.create_hitmark(self.x, self.y, "Unlocked!")
        else:
            if self.state == "idle":
                self.boop()
            if self.state == "buzzing":
                self.answer_buzz()

    def boop(self):
        self.idle_time = 0
        ScoreHandler.increase_score(5)

    def unlock(self):
        self.state = "idle"
        self.locked_state = False
        self.idle_time = 0

    def answer_buzz(self):
        self.set_new_buzz_timer()
        self.state = "idle"
        self.idle_time = 0
        UIHandler.create_hitmark(self.x, self.y, "Call answered!")
        ScoreHandler.increase_score(self.answer_buzz_score)

    def lock(self):
        self.locked_state = True
        self.state = "locked"
        UIHandler.create_hitmark(self.x, self.y, "Computer locked!")

    def set_new_buzz_timer(self):
        self.time_to_buzz = self.max_buzz_timer

    def start_buzzing(self):
        self.state = "buzzing"

    def get_pos(self):
        return self.x, self.y
