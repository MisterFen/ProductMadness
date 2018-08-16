import pygame
import random
import ScoreHandler, UIHandler, Config, GameLogic, SparkleHandler


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

    get_back_to_work_score = 19
    on_shout_score = 19
    max_time_working_limit = 3000

    def __init__(self, x, y, direction):
        self.x = self.start_x = self.target_x = x
        self.y = self.start_y = self.target_y = y
        self.width = 38
        self.height = 38
        self.state = "working"
        self.time_working = 0
        self.time_working_limit = random.randint(300, self.max_time_working_limit)
        self.time_since_rotated = 0
        self.rotate_increment = 90
        self.angle = 90
        self.img_rect = self.img.get_rect()
        self.set_image()
        self.speed = 1
        self.times_rotated = 0
        self.starting_direction = direction
        self.moving_left = self.moving_right = self.moving_down = self.moving_up = False

    def on_start(self):
        self.x = self.start_x
        self.y = self.start_y
        self.state = "working"
        self.time_working = 0
        self.time_working_limit = random.randint(300, self.max_time_working_limit)
        self.time_since_rotated = 0
        self.img_rect = self.img.get_rect()
        self.set_image()
        self.speed = 1
        self.times_rotated = 0
        self.face_starting_direction()

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
                self.time_working = 0
                self.state = "working"
                self.face_starting_direction()
                self.stopped_moving()

    def move_toward_y(self, y):
        if self.y < y:
            self.moving_up = True
            self.moving_down = False
            self.y += self.speed
            if y - self.y < 1:
                self.y = y
        elif self.y > y:
            self.moving_down = True
            self.moving_up = False
            self.y -= self.speed
            if self.y - y < 1:
                self.y = y

    def move_toward_x(self, x):
        if self.x < x:
            self.moving_right = True
            self.moving_left = False
            self.x += self.speed
            if x - self.x < 1:
                self.x = x
        elif self.x > x:
            self.moving_right = False
            self.moving_left = True
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
        if self.state == "sparkling":
            SparkleHandler.draw_passive_sparkle(display, self.get_pos())

    def rotate(self):
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.times_rotated += 1
        if self.times_rotated == 4:
            self.times_rotated = 0

    def face_starting_direction(self):
        if self.starting_direction == "left":
            self.face_left()
        elif self.starting_direction == "right":
            self.face_right()
        else:
            self.face_left()
            print("NO STARTING DIRECTION!>!>!??")

    def face_left(self):
        while self.times_rotated != 1:
            self.rotate()

    def face_right(self):
        while self.times_rotated != 3:
            self.rotate()

    def on_player_interact(self):
        ScoreHandler.increase_score(1)
        if self.state == "spinning":
            self.return_to_work_from_spinning(self.get_back_to_work_score)
        elif self.state == "working":
            self.boop()
        elif self.state == "pacing":
            self.walk_back_to_desk(self.get_back_to_work_score)
        elif self.state =="sparkling":
            self.on_sparkle_interact()

    def on_shout(self):
        if self.state == "spinning":
            self.return_to_work_from_spinning(self.on_shout_score)
        elif self.state == "working":
            self.boop()
        elif self.state == "pacing":
            self.walk_back_to_desk(self.on_shout_score)

    def on_sparkle(self):
        SparkleHandler.sparkle_target_pos = self.get_pos()

    def on_passive_sparkle(self):
        self.state = "sparkling"

    def boop(self):
        self.time_working = 0

    def walk_back_to_desk(self, score):
        self.state = "returning"
        self.time_working = 0
        UIHandler.create_hitmark(self.x - 50, self.y - 15, "Returning to desk")
        ScoreHandler.increase_score(score)

    def return_to_work_from_spinning(self, score):
        self.back_to_work()
        UIHandler.create_hitmark(self.x - 50, self.y - 15, "Stopped Spinning!")
        ScoreHandler.increase_score(score)

    def back_to_work(self):
        self.state = "working"
        self.time_working = 0
        self.face_starting_direction()

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

    def on_sparkle_interact(self):
        self.back_to_work()
        UIHandler.create_hitmark(self.x - 50, self.y - 15, "Sparkle Acknowledged!")
        SparkleHandler.sparkles_used += 1
        ScoreHandler.increase_score(99)

    def get_pos(self):
        return self.x, self.y

    def stopped_moving(self):
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False