import Config, GameLogic
import pygame
from CollisionHandler import check_object_collision
from ObjectHandler import tables
import TargetHandler


class Player:
    img = idle_image = pygame.image.load('art/player.png')
    score_up_vfx = pygame.image.load('art/score_up_vfx.png')
    walking_image1 = pygame.image.load('art/player_walking1.png')
    walking_image2 = pygame.image.load('art/player_walking2.png')
    walking_images = [walking_image1, walking_image2]

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
        self.moving_index = 0
        self.time_moving = 0
        self.walking_anim_speed = 6
        self.last_direction = "down"
        self.rotate_index = 0
        self.expected_rotate_index = 0

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
        if self.moving_up:
            self.y -= self.speed
            self.last_direction = "up"
            if check_object_collision(self, tables):
                self.y += self.speed
        if self.moving_down:
            self.y += self.speed
            self.last_direction = "down"
            if check_object_collision(self, tables):
                self.y -= self.speed
        if self.moving_left:
            self.x -= self.speed
            self.last_direction = "left"
            if check_object_collision(self, tables):
                self.x += self.speed
        if self.moving_right:
            self.x += self.speed
            self.last_direction = "right"
            if check_object_collision(self, tables):
                self.x -= self.speed

        if self.is_moving():
            self.time_moving += 1
            if self.time_moving >= self.walking_anim_speed:
                self.time_moving = 0
                self.moving_index += 1
                if self.moving_index > len(self.walking_images):
                    self.moving_index = 0

            if self.moving_index == 0:
                self.img = self.walking_images[0]
            elif self.moving_index == 1:
                self.img = self.walking_images[1]
        else:
            self.img = self.idle_image
            self.time_moving = 0

        self.face_last_direction()

        display.blit(self.img, (self.x, self.y))
        TargetHandler.draw_interaction_icon_for(self)

        if GameLogic.score_up_active:
            display.blit(self.score_up_vfx, self.get_pos())

    def interact(self):
        if GameLogic.time_since_last_interact > GameLogic.max_interact_timer:
            if TargetHandler.get_closest_target_range(self) <= self.target_range:
                TargetHandler.get_closest_target(self).on_player_interact()
                GameLogic.time_since_last_interact = 0

    def use_ability(self, int):
        if int == 1:
            GameLogic.use_shout(self.x, self.y)
        if int == 2:
            GameLogic.use_extend_deadline(self.x, self.y)
        if int == 3:
            GameLogic.use_score_up()
        if int == 4:
            GameLogic.use_sparkle()

    def face_last_direction(self):
        if self.last_direction == "left":
            self.expected_rotate_index = 1
        elif self.last_direction == "up":
            self.expected_rotate_index = 2
        elif self.last_direction == "right":
            self.expected_rotate_index = 3
        elif self.last_direction == "down":
            self.expected_rotate_index = 0
        while self.rotate_index != self.expected_rotate_index:
            self.rotate()

    def rotate(self):
        print("Rotated!")
        self.img = pygame.transform.rotate(self.img, 90)
        self.rotate_index += 1
        if self.rotate_index >= 4:
            self.rotate_index = 0

    def get_pos(self):
        return self.x, self.y

    def is_moving(self):
        if self.moving_left:
            return True
        elif self.moving_right:
            return True
        elif self.moving_down:
            return True
        elif self.moving_up:
            return True
        else:
            return False
