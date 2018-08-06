import pygame
import Config, ScoreHandler, GameLogic
from Hitmark import Hitmark
from Button import Button


hitmarks = []

button1 = Button(250, 500, 100, 50, "Play")
button2 = Button(450, 500, 100, 50, "Quit")

title_image = pygame.image.load('art/title_image.png')
title_image_x = 200
title_image_y = 50
title_images = [title_image]
title_buttons = [button1, button2]

hud_background_image = pygame.image.load('art/ui_bar.png')
timer_box_image = pygame.image.load('art/timer_box.png')

ability_box_image = pygame.image.load('art/ability_box.png')
interact_ability_image = pygame.image.load('art/interact_ability.png')
shout_ability_image = pygame.image.load('art/shout_ability.png')
extend_deadline_ability_image = pygame.image.load('art/deadline_ability.png')
score_up_ability_image = pygame.image.load('art/score_up_ability.png')
sparkle_ability_image = pygame.image.load('art/sparkle_ability.png')




def draw(display):
    purge_hitmarks()
    draw_hitmarks(display)
    draw_hud(display)


def draw_score(display):
    font_size = 22
    pygame.font.init()
    my_font = pygame.font.SysFont('Verdana', font_size)
    text_surface = my_font.render('Score: ' + str(ScoreHandler.score), False, (0, 0, 0))
    display.blit(text_surface, (10, Config.display_height - font_size - 10))


def draw_hitmarks(display):
    for x in hitmarks:
        x.draw(display)


def create_hitmark(x, y, msg):
    hitmark = Hitmark(x, y, msg)
    hitmarks.append(hitmark)


def check_title_buttons_clicked():
    x, y = pygame.mouse.get_pos()
    for i in title_buttons:
        if x < i.rect.x + i.rect.width:
            if x > i.rect.x:
                if y < i.rect.y + i.rect.height:
                    if y > i.rect.y:
                        return i.text


def purge_hitmarks():
    for x in hitmarks:
        if x.time_active > x.max_time_active:
            hitmarks.remove(x)
            del x


def draw_title(display):
    display.fill((200, 200, 200))
    display.blit(title_image, (title_image_x, title_image_y))
    for x in title_buttons:
        x.draw(display)


def draw_hud(display):
    display.blit(hud_background_image, (0, 500))
    draw_game_timer(display)
    draw_score(display)
    draw_abilities(display)


def draw_abilities(display):
    draw_default_interaction(display)
    draw_shout(display)
    draw_extend_deadline(display)
    draw_score_up(display)
    draw_sparkle(display)


def draw_default_interaction(display):
    pos = (250, 542)
    display.blit(interact_ability_image, pos)
    display.blit(ability_box_image, pos)
    time_until_can_interact = GameLogic.max_interact_timer - GameLogic.time_since_last_interact
    if time_until_can_interact < 0:
        time_until_can_interact = 0
    s = pygame.Surface((54, 54 * (time_until_can_interact / GameLogic.max_interact_timer)))
    s.set_alpha(230)
    s.fill((128, 128, 128))
    display.blit(s, pos)


def draw_shout(display):
    pos = (360, 542)
    display.blit(shout_ability_image, pos)
    display.blit(ability_box_image, pos)
    time_until_can_use_ability = GameLogic.max_ability_timer - GameLogic.time_since_last_ability
    if time_until_can_use_ability < 0:
        time_until_can_use_ability = 0
    s = pygame.Surface((54, 54 * (time_until_can_use_ability / GameLogic.max_ability_timer)))
    s.set_alpha(230)
    s.fill((128, 128, 128))
    display.blit(s, pos)


def draw_extend_deadline(display):
    pos = (420, 542)
    display.blit(extend_deadline_ability_image, pos)
    display.blit(ability_box_image, pos)
    time_until_can_use_ability = GameLogic.max_ability_timer - GameLogic.time_since_last_ability
    if time_until_can_use_ability < 0:
        time_until_can_use_ability = 0
    s = pygame.Surface((54, 54 * (time_until_can_use_ability / GameLogic.max_ability_timer)))
    s.set_alpha(230)
    s.fill((128, 128, 128))
    display.blit(s, pos)


def draw_score_up(display):
    pos = (480, 542)
    display.blit(score_up_ability_image, pos)
    display.blit(ability_box_image, pos)
    time_until_can_use_ability = GameLogic.max_ability_timer - GameLogic.time_since_last_ability
    if time_until_can_use_ability < 0:
        time_until_can_use_ability = 0
    s = pygame.Surface((54, 54 * (time_until_can_use_ability / GameLogic.max_ability_timer)))
    s.set_alpha(230)
    s.fill((128, 128, 128))
    display.blit(s, pos)


def draw_sparkle(display):
    pos = (540, 542)
    display.blit(sparkle_ability_image, pos)
    display.blit(ability_box_image, pos)
    time_until_can_use_ability = GameLogic.max_ability_timer - GameLogic.time_since_last_ability
    if time_until_can_use_ability < 0:
        time_until_can_use_ability = 0
    s = pygame.Surface((54, 54 * (time_until_can_use_ability / GameLogic.max_ability_timer)))
    s.set_alpha(230)
    s.fill((128, 128, 128))
    display.blit(s, pos)


def draw_game_timer(display):
    #Text
    font_size = 22
    pygame.font.init()
    my_font = pygame.font.SysFont('Verdana', font_size)
    text_surface = my_font.render('Deadline: ', False, (0, 0, 0))
    display.blit(text_surface, (10, 510))
    #Box
    display.blit(timer_box_image, (125, 510))
    #Inner box
    inner_box_rect = pygame.__rect_constructor(126, 511, (648*(GameLogic.current_timer/GameLogic.start_timer)), 28)
    pygame.draw.rect(display, (175, 32, 24), inner_box_rect, 0)