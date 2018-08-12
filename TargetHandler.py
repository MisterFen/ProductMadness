from NPCHandler import devs
from ObjectHandler import interactable_objects
import math, UIHandler

targets = []

for x in devs:
    targets.append(x)

for x in interactable_objects:
    targets.append(x)


def get_closest_target_range(player):
    closest_range = 100000
    for x in targets:
        distance = get_range(x, player)
        if distance < closest_range:
            closest_range = distance
    return closest_range


def get_closest_target_in_range(player):
    closest_range = 100000
    closest_target = 0
    for x in targets:
        distance = get_range(x, player)
        if distance < closest_range:
            closest_range = distance
            closest_target = x
    if closest_range < player.target_range:
        return closest_target
    else:
        return 0


def get_closest_target(player):
    closest_range = 100000
    closest_target = 0
    for x in targets:
        distance = get_range(x, player)
        if distance < closest_range:
            closest_range = distance
            closest_target = x
    return closest_target


def get_range(target, player):
    x_diff = player.x - target.x
    y_diff = player.y - target.y

    if x_diff < 0:
        x_diff *= -1

    if y_diff < 0:
        y_diff *= -1

    range = math.sqrt((x_diff * x_diff) + (y_diff * y_diff))
    return range


def draw_interaction_icon_for(player):
    target = get_closest_target_in_range(player)
    if target != 0:
        UIHandler.draw_interaction_icon_for(target.get_pos())
    else:
        UIHandler.purge_interaction_icons()
