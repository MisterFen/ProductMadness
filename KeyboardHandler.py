import pygame

x_change = 0;
y_change = 0;

def on_event(event, player):
    global x_change
    global y_change

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change -= player.speed
        if event.key == pygame.K_RIGHT:
            x_change += player.speed
        if event.key == pygame.K_UP:
            y_change -= player.speed
        if event.key == pygame.K_DOWN:
            y_change += player.speed

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            x_change += player.speed
        if event.key == pygame.K_RIGHT:
            x_change -= player.speed
        if event.key == pygame.K_UP:
            y_change += player.speed
        if event.key == pygame.K_DOWN:
            y_change -= player.speed


def on_event_end(player):
    global x_change
    global y_change
    player.x += x_change
    player.y += y_change