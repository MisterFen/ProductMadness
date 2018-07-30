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


def on_tick():
    NPCHandler.on_tick()
    ObjectHandler.on_tick()


def main():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            KeyboardHandler.on_event(event, player)
        on_tick()
        draw()

        pygame.display.update()
        clock.tick(Config.FPS)


main()

pygame.quit()
quit()
