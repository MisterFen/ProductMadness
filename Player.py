import Config, GameLogic
import pygame
from CollisionHandler import check_object_collision
from ObjectHandler import tables
import TargetHandler


class Player:
    img = idle_image = pygame.image.load('art/player_idle_down.png')
    idle_image_down = pygame.image.load('art/player_idle_down.png')
    idle_image_up = pygame.image.load('art/player_idle_up.png')
    idle_image_left = pygame.image.load('art/player_idle_left.png')
    idle_image_right = pygame.image.load('art/player_idle_right.png')

    score_up_vfx = pygame.image.load('art/score_up_vfx.png')
    walking_left_image_1 = pygame.image.load('art/player_walking_left_1.png')
    walking_left_image_2 = pygame.image.load('art/player_walking_left_2.png')
    walking_left_images = [walking_left_image_1, walking_left_image_2]
    walking_right_image_1 = pygame.image.load('art/player_walking_right_1.png')
    walking_right_image_2 = pygame.image.load('art/player_walking_right_2.png')
    walking_right_images = [walking_right_image_1, walking_right_image_2]
    walking_down_image_1 = pygame.image.load('art/player_walking_down_1.png')
    walking_down_image_2 = pygame.image.load('art/player_walking_down_2.png')
    walking_down_images = [walking_down_image_1, walking_down_image_2]
    walking_up_image_1 = pygame.image.load('art/player_walking_up_1.png')
    walking_up_image_2 = pygame.image.load('art/player_walking_up_2.png')
    walking_up_images = [walking_up_image_1, walking_up_image_2]

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
        anim_array = []
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

        if self.moving_left:
            anim_array = self.walking_left_images
        elif self.moving_right:
            anim_array = self.walking_right_images
        elif self.moving_down:
            anim_array = self.walking_down_images
        elif self.moving_up:
            anim_array = self.walking_up_images

        if self.is_moving():
            self.time_moving += 1
            if self.time_moving >= self.walking_anim_speed:
                self.time_moving = 0
                self.moving_index += 1
                if self.moving_index > len(anim_array):
                    self.moving_index = 0

            if self.moving_index == 0:
                self.img = anim_array[0]
            elif self.moving_index == 1:
                self.img = anim_array[1]
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

    def use_ability(self, num):
        if num == 1:
            GameLogic.use_shout(self.x, self.y)
        if num == 2:
            GameLogic.use_extend_deadline(self.x, self.y)
        if num == 3:
            GameLogic.use_score_up()
        if num == 4:
            GameLogic.use_sparkle()

    def face_last_direction(self):
        if self.last_direction == "left":
            self.idle_image = self.idle_image_left
        elif self.last_direction == "up":
            self.idle_image = self.idle_image_up
        elif self.last_direction == "right":
            self.idle_image = self.idle_image_right
        elif self.last_direction == "down":
            self.idle_image = self.idle_image_down

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
