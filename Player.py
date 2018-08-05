import Config, GameLogic
import pygame
from CollisionHandler import check_object_collision
from ObjectHandler import objects
import TargetHandler

class Player:
    img = pygame.image.load('art/player.png')

    def __init__(self):
        self.x = Config.player_start_x
        self.y = Config.player_start_y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.img_rect = self.img.get_rect()
        self.target_range = 50
        self.time_since_last_interact = 0

    def on_start(self):
        self.x = Config.player_start_x
        self.y = Config.player_start_y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.img_rect = self.img.get_rect()
        self.time_since_last_interact = 0

    def draw(self, display):
        if self.moving_left:
            self.x -= self.speed
            if check_object_collision(self, objects):
                self.x += self.speed
        if self.moving_right:
            self.x += self.speed
            if check_object_collision(self, objects):
                self.x -= self.speed
        if self.moving_up:
            self.y -= self.speed
            if check_object_collision(self, objects):
                self.y += self.speed
        if self.moving_down:
            self.y += self.speed
            if check_object_collision(self, objects):
                self.y -= self.speed

        display.blit(self.img, (self.x, self.y))

    def interact(self):
        if GameLogic.time_since_last_interact > GameLogic.max_interact_timer:
            if TargetHandler.get_closest_target_range(self) <= self.target_range:
                TargetHandler.get_closest_target(self).on_player_interact()
                GameLogic.time_since_last_interact = 0

    def use_ability(self, int):
        if GameLogic.time_since_last_ability > GameLogic.max_ability_timer:
            if int == 1:
                GameLogic.use_shout()
            if int == 2:
                GameLogic.use_extend_deadline()
            if int == 3:
                GameLogic.use_score_up()
            if int == 4:
                GameLogic.use_sparkle()
