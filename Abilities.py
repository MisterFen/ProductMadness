import GameLogic, ScoreHandler, NPCHandler, SparkleHandler, UIHandler
import random
import pygame

score_up_duration = 100
score_up_multiplier = 3

shout_pos_x = 0
shout_pos_y = 0

shout_img = pygame.image.load('art/shout.png')


def use_extend_deadline(x, y):
    random.seed()
    max_deadline_increase = 200
    remaining_time_percentage = 1-(GameLogic.current_timer / GameLogic.start_timer)
    amount_to_increase = int(remaining_time_percentage * max_deadline_increase)
    amount_to_increase += random.randint(3, 30)
    GameLogic.current_timer += amount_to_increase
    UIHandler.create_image_hitmark("extend deadline", x, y)

def use_score_up():
    ScoreHandler.set_score_modifier(score_up_multiplier)


def use_shout(x, y):
    global shout_pos_x, shout_pos_y
    NPCHandler.on_shout()
    GameLogic.last_shout = 0
    shout_pos_x = x
    shout_pos_y = y


def use_sparkle():
    SparkleHandler.on_use()


def draw(display):
    if GameLogic.sparkle_active:
        SparkleHandler.draw(display)
    if GameLogic.last_shout < 35:
        display.blit(shout_img, (shout_pos_x - 50, shout_pos_y - 50))
