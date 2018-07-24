import pygame
import time
import Config, BackgroundHandler
from Player import Player

pygame.init()

gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
pygame.display.set_caption(Config.game_title)
clock = pygame.time.Clock()

BackgroundHandler.set_background()
player = Player()

def draw():
    BackgroundHandler.draw_background(gameDisplay)
    player.draw(gameDisplay)

def main():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        draw()

        pygame.display.update()
        clock.tick(Config.FPS)

main()

pygame.quit()
quit()
