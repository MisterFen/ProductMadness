import pygame
import Config, BackgroundHandler, ObjectHandler, KeyboardHandler, NPCHandler, UIHandler
from Player import Player

pygame.init()

gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
pygame.display.set_caption(Config.game_title)
clock = pygame.time.Clock()

BackgroundHandler.set_background()

player = Player()


def draw():
    BackgroundHandler.draw_background(gameDisplay)
    ObjectHandler.draw_objects(gameDisplay)
    NPCHandler.draw_npcs(gameDisplay)
    player.draw(gameDisplay)
    UIHandler.draw(gameDisplay)


def display_title():
    UIHandler.draw_title(gameDisplay)
    pygame.display.update()
    clock.tick(Config.FPS)


def on_tick():
    NPCHandler.on_tick()
    ObjectHandler.on_tick()


def main():
    game_running = False
    game_exit = False

    while not game_exit:

        display_title()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if UIHandler.check_title_buttons_clicked() == "Play":
                    game_running = True
                elif UIHandler.check_title_buttons_clicked() == "Quit":
                    game_running = False
                    game_exit = True

        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_running = False
                    game_exit = True
                KeyboardHandler.on_event(event, player)
            on_tick()
            draw()

            pygame.display.update()
            clock.tick(Config.FPS)


main()

pygame.quit()
quit()
