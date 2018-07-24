import pygame
import time
import Config, BackgroundHandler

pygame.init()

gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
pygame.display.set_caption(Config.game_title)
clock = pygame.time.Clock()

BackgroundHandler.set_background()

def draw():
    BackgroundHandler.draw_background(gameDisplay)

def main():
    gameExit = False
    while not gameExit:
        draw()
        pygame.display.update()
        clock.tick(60)
        print('Clock ticked')

main()
pygame.quit()
quit()