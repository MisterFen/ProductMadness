import pygame
import random
import ScoreHandler, UIHandler, Config


class NPC:
    img = pygame.image.load('art/default.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, display):
        display.blit(self.img, (self.x, self.y))


class Dev(NPC):
    random.seed()
    img = pygame.image.load('art/dev1.png')

    get_back_to_work_score = 49

    def __init__(self, x, y):
        self.x = self.start_x = self.target_x = x
        self.y = self.start_y = self.target_y = y
        self.width = 38
        self.height = 38
        self.state = "working"
        self.time_working = 0
        self.time_working_limit = random.randint(300, 1000)
        self.time_since_rotated = 0
        self.rotate_increment = 90
        self.angle = 90
        self.img_rect = self.img.get_rect()
        self.set_image()
        self.speed = 1

    def on_tick(self):
        if self.state == "working":
            self.time_working += 1
            if self.time_working >= self.time_working_limit:
                self.state = self.choose_random_slacking_state()
        if self.state == "spinning":
            self.time_since_rotated += 1
            if self.time_since_rotated >= self.rotate_increment:
                self.rotate()
                self.time_since_rotated = 0
        if self.state == "pacing":
            if self.y != Config.aisle_middle_y:
                self.move_toward_y(Config.aisle_middle_y)
            else:
                if self.x != self.target_x:
                    self.move_toward_x(self.target_x)
                else:
                    self.set_target_x()

        if self.state == "returning":
            if self.x != self.start_x:
                self.move_toward_x(self.start_x)
            elif self.y != self.start_y:
                self.move_toward_y(self.start_y)

            if (self.y == self.start_y) and (self.x == self.start_x):
                UIHandler.create_hitmark(self.x, self.y, "Working...")
                self.state = "working"

    def move_toward_y(self, y):
        if self.y < y:
            self.y += self.speed
            if y - self.y < 1:
                self.y = y
        elif self.y > y:
            self.y -= self.speed
            if self.y - y < 1:
                self.y = y

    def move_toward_x(self, x):
        if self.x < x:
            self.x += self.speed
            if x - self.x < 1:
                self.x = x
        elif self.x > x:
            self.x -= self.speed
            if self.x - x < 1:
                self.x = x

    def set_target_x(self):
        if self.x < Config.aisle_middle_x:
            self.target_x = Config.display_width - 75
        elif self.x > Config.aisle_middle_x:
            self.target_x = 75

    def draw(self, display):
        display.blit(self.img,(self.x, self.y))

    def rotate(self):
        self.img = pygame.transform.rotate(self.img, self.angle)

    def on_player_interact(self):
        ScoreHandler.increase_score(1)
        if self.state == "spinning":
            self.get_back_to_work()
        elif self.state == "working":
            self.boop()
        elif self.state == "pacing":
            self.walk_back_to_desk()

    def boop(self):
        print('Boop')

    def walk_back_to_desk(self):
        self.state = "returning"
        self.time_working = 0
        UIHandler.create_hitmark(self.x - 50, self.y - 15, "Returning to desk")
        ScoreHandler.increase_score(self.get_back_to_work_score)

    def get_back_to_work(self):
        self.state = "working"
        self.time_working = 0
        UIHandler.create_hitmark(self.x - 50, self.y - 15, "Stopped Spinning!")
        ScoreHandler.increase_score(self.get_back_to_work_score)

    def set_image(self):
        random_number = random.randint(1, 4)
        if random_number == 1:
            self.img = pygame.image.load('art/dev1.png')
        elif random_number == 2:
            self.img = pygame.image.load('art/dev2.png')
        elif random_number == 3:
            self.img = pygame.image.load('art/dev3.png')
        else:
            self.img = pygame.image.load('art/dev4.png')

    def choose_random_slacking_state(self):
        random_number = random.randint(0, 100)
        if 10 <= random_number <= 100:
            return "spinning"
        elif 0 <= random_number <= 9:
            return "pacing"
        else:
            return "spinning"
