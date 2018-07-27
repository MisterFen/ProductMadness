import Config
import pygame
from CollisionHandler import check_object_collision
from ObjectHandler import objects


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
