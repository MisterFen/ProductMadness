import pygame
import Config, ScoreHandler, GameLogic
from Hitmark import Hitmark
from Button import Button
from AbilityUnreadyOverlay import AbilityUnreadyOverlay
from InteractionIcon import InteractionIcon

hitmarks = []
overlays = []
interaction_icons = []

interaction_icon_displaying = False

selected_target = 0
active_target = 0

button1 = Button(150, 500, 100, 50, "Play")
button2 = Button(350, 500, 100, 50, "How to play")
button3 = Button(550, 500, 100, 50, "Quit")

high_score_button1 = Button(300, 500, 100, 50, "Finish")

how_to_play_button1 = Button(300, 535, 100, 50, "Back")

title_image = pygame.image.load('art/title_image.png')
title_image_x = 200
title_image_y = 50
title_images = [title_image]
title_buttons = [button1, button2, button3]

high_score_buttons = [high_score_button1]

how_to_play_buttons = [how_to_play_button1]

hud_background_image = pygame.image.load('art/ui_bar.png')
timer_box_image = pygame.image.load('art/timer_box.png')

ability_box_image = pygame.image.load('art/ability_box.png')
interact_ability_image = pygame.image.load('art/interact_ability.png')
shout_ability_image = pygame.image.load('art/shout_ability.png')
extend_deadline_ability_image = pygame.image.load('art/deadline_ability.png')
score_up_ability_image = pygame.image.load('art/score_up_ability.png')
sparkle_ability_image = pygame.image.load('art/sparkle_ability.png')

ability_label_e_img = pygame.image.load('art/ability_letter_e.png')
ability_label_1_img = pygame.image.load('art/ability_number_1.png')
ability_label_2_img = pygame.image.load('art/ability_number_2.png')
ability_label_3_img = pygame.image.load('art/ability_number_3.png')
ability_label_4_img = pygame.image.load('art/ability_number_4.png')


def draw(display):
    purge_hitmarks()
    draw_hitmarks(display)
    draw_interaction_icons(display)
    draw_hud(display)
    purge_overlays()


def draw_score(display):
    font_size = 22
    pygame.font.init()
    my_font = pygame.font.SysFont('Verdana', font_size)
    text_surface = my_font.render('Score: ' + str(ScoreHandler.score), False, (0, 0, 0))
    display.blit(text_surface, (10, Config.display_height - font_size - 10))


def draw_hitmarks(display):
    for x in hitmarks:
        x.draw(display)


def draw_overlays(display):
    for x in overlays:
        display.blit(x.get_surface(), (x.x, x.y))
        x.on_tick()


def draw_interaction_icons(display):
    for x in interaction_icons:
        display.blit(x.get_image(), x.pos)
        x.on_tick()


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


def check_high_score_buttons_clicked():
    x, y = pygame.mouse.get_pos()
    for i in high_score_buttons:
        if x < i.rect.x + i.rect.width:
            if x > i.rect.x:
                if y < i.rect.y + i.rect.height:
                    if y > i.rect.y:
                        return i.text


def check_how_to_play_buttons_clicked():
    x, y = pygame.mouse.get_pos()
    for i in how_to_play_buttons:
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


def purge_overlays():
    for x in overlays:
        if x.time_active > x.max_time_active:
            overlays.remove(x)
            del x


def purge_interaction_icons():
    if len(interaction_icons) > 0:
        for x in interaction_icons:
            interaction_icons.remove(x)
            del x


def draw_title_screen(display):
    display.fill((200, 200, 200))
    display.blit(title_image, (title_image_x, title_image_y))
    for x in title_buttons:
        x.draw(display)


def draw_high_score_screen(display):
    display.fill((200, 200, 200))
    draw_message(display, 250, 300, 36, "Your score was: "+str(ScoreHandler.score))
    for x in high_score_buttons:
        x.draw(display)


def draw_how_to_play_screen(display):
    display.fill((200, 200, 200))
    draw_message(display, 285, 20, 36, "How to play ")
    for x in how_to_play_buttons:
        x.draw(display)
    draw_message(display, 50, 80, 16, "Move around using the WASD or Arrow Keys")
    draw_message(display, 50, 105, 16, "Interact with objects and people to get the project out before the deadline runs out")
    draw_message(display, 50, 130, 16, "Use the following abilities to increase your productivity: ")
    display.blit(interact_ability_image, (50, 160))
    draw_message(display, 115, 170, 16, "(E) Interact: Interact with nearby objects or people")
    display.blit(shout_ability_image, (50, 230))
    draw_message(display, 115, 240, 16, "(1) Shout: Make everyone back to work instantly")
    display.blit(extend_deadline_ability_image, (50, 300))
    draw_message(display, 115, 310, 16, "(2) Extend Deadline: Increase the deadline timer slightly")
    display.blit(score_up_ability_image, (50, 370))
    draw_message(display, 115, 380, 16, "(3) Score Up: Multiply the amount of score gained for a short period")
    display.blit(sparkle_ability_image, (50, 440))
    draw_message(display, 115, 450, 16, "(4) Sparkle: SPAAAAAAAAAAAAAAAARRRRRRRRKLLEEEEEEEEEEE!!!!!!!!")


def draw_message(display, x, y, size, text):
    font_size = size
    pygame.font.init()
    my_font = pygame.font.SysFont('Verdana', font_size)
    text_surface = my_font.render(text, False, (0, 0, 0))
    display.blit(text_surface, (x, y))


def draw_hud(display):
    display.blit(hud_background_image, (0, 500))
    draw_game_timer(display)
    draw_score(display)
    draw_abilities(display)
    draw_overlays(display)


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
    display.blit(ability_label_e_img, pos)


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
    display.blit(ability_label_1_img, pos)


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
    display.blit(ability_label_2_img, pos)


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
    display.blit(ability_label_3_img, pos)


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
    display.blit(ability_label_4_img, pos)


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


def on_unready_ability_trigger(num):
    pos = (0, 0)
    if num == 1:
        pos = (360, 542)
    elif num == 2:
        pos = (420, 542)
    elif num == 3:
        pos = (480, 542)
    elif num == 4:
        pos = (540, 542)
    overlay = AbilityUnreadyOverlay(pos, 1)
    overlays.append(overlay)


def draw_interaction_icon_for(target):
    global active_target
    if active_target != target:
        active_target = target
        interaction_icon = InteractionIcon(target)
        interaction_icons.append(interaction_icon)
    if len(interaction_icons) == 0:
        interaction_icon = InteractionIcon(target)
        interaction_icons.append(interaction_icon)
    if len(interaction_icons) > 1:
        interaction_icons.pop(0)
