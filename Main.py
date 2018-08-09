import pygame
import Config, BackgroundHandler, ObjectHandler, KeyboardHandler, NPCHandler, UIHandler, GameLogic
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
    UIHandler.draw_title_screen(gameDisplay)
    pygame.display.update()
    clock.tick(Config.FPS)


def display_high_score_screen():
    UIHandler.draw_high_score_screen(gameDisplay)
    pygame.display.update()
    clock.tick(Config.FPS)

def on_tick():
    NPCHandler.on_tick()
    ObjectHandler.on_tick()
    GameLogic.on_tick()


def main():
    game_exit = False

    while not game_exit:

        display_title()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if UIHandler.check_title_buttons_clicked() == "Play":
                    GameLogic.on_start()
                    player.on_start()
                elif UIHandler.check_title_buttons_clicked() == "Quit":
                    GameLogic.game_running = False
                    game_exit = True

        while GameLogic.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameLogic.game_running = False
                    game_exit = True
                KeyboardHandler.on_event(event, player)
            on_tick()
            draw()

            pygame.display.update()
            clock.tick(Config.FPS)

        while GameLogic.state == "high score":
            display_high_score_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameLogic.state = "quit"
                    game_exit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if UIHandler.check_high_score_buttons_clicked() == "Finish":
                        GameLogic.state = "title"


main()

pygame.quit()
quit()
