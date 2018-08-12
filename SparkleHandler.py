import pygame
import random
import NPCHandler

sparkles_used = 0
last_sparkle = 0
timer = 0
sparkle_target_pos = (0, 0)

big_sparkle_image = pygame.image.load("art/big_sparkle.png")
small_sparkle_image = pygame.image.load("art/small_sparkle.png")
passive_sparkle_image = pygame.image.load("art/passive_sparkle.png")


def on_use():
    global timer
    random_number = random.randint(1, 3)
    print(random_number)
    timer = random.randint(10, 50)
    if random_number == 1:
        set_sparkle("small")
        print("Small")
    elif random_number == 2:
        set_sparkle("big")
        print("Big")
    elif random_number == 3:
        set_sparkle("passive")
        print("Passive")


def set_sparkle(size):
    global last_sparkle
    if size == "small":
        last_sparkle = size
        NPCHandler.get_random_dev().on_sparkle()
    elif size == "big":
        last_sparkle = size
    elif size == "passive":
        last_sparkle = size
        NPCHandler.get_random_dev().on_passive_sparkle()


def draw(display):
    global last_sparkle
    if last_sparkle == "big":
        display.blit(big_sparkle_image, (0, 0))
    elif last_sparkle == "small":
        display.blit(small_sparkle_image, sparkle_target_pos)


def draw_passive_sparkle(display, pos):
    display.blit(passive_sparkle_image, pos)
