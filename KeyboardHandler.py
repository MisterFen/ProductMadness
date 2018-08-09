import pygame
import GameLogic, UIHandler


def on_event(event, player):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            player.moving_left = True
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            player.moving_right = True
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            player.moving_up = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            player.moving_down = True
        if event.key == pygame.K_e:
            player.interact()
        if event.key == pygame.K_1:
            if GameLogic.time_since_last_ability > GameLogic.max_ability_timer:
                player.use_ability(1)
            else:
                UIHandler.on_unready_ability_trigger(1)
        if event.key == pygame.K_2:
            if GameLogic.time_since_last_ability > GameLogic.max_ability_timer:
                player.use_ability(2)
            else:
                UIHandler.on_unready_ability_trigger(2)
        if event.key == pygame.K_3:
            if GameLogic.time_since_last_ability > GameLogic.max_ability_timer:
                player.use_ability(3)
            else:
                UIHandler.on_unready_ability_trigger(3)
        if event.key == pygame.K_4:
            if GameLogic.time_since_last_ability > GameLogic.max_ability_timer:
                player.use_ability(4)
            else:
                UIHandler.on_unready_ability_trigger(4)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            player.moving_left = False
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            player.moving_right = False
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            player.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            player.moving_down = False
