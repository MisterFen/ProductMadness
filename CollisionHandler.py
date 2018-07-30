import Config


def check_object_collision(player, objects):
    # Objects collision
    for i in objects:
        if check_collision(player, i):
            return True

    # Boundary collision
    if player.x < 0:
        return True
    if player.x + player.width > Config.display_width:
        return True
    if player.y < 0:
        return True
    if player.y + player.height > Config.display_height:
        return True


def check_collision(player, object):
    if player.x < object.x + object.width:
        if player.x + player.width > object.x:
            if player.y < object.y + object.height:
                if player.y + player.height > object.y:
                    return True
