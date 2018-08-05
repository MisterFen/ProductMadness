import NPCHandler
import ObjectHandler
import ScoreHandler

game_running = False

start_timer = 10000
current_timer = start_timer
time_since_last_interact = max_interact_timer = 50
time_since_last_ability = 0
max_ability_timer = 500


def on_tick():
    global current_timer, game_running, time_since_last_interact, time_since_last_ability
    current_timer -= 1
    if current_timer <= 0:
        game_running = False
    time_since_last_interact += 1
    time_since_last_ability += 1


def on_start():
    global game_running, current_timer
    game_running = True
    current_timer = start_timer
    NPCHandler.reset()
    ObjectHandler.reset()
    ScoreHandler.reset()


def on_use_ability():
    global time_since_last_ability
    time_since_last_ability = 0


def use_shout():
    on_use_ability()


def use_extend_deadline():
    on_use_ability()


def use_score_up():
    on_use_ability()


def use_sparkle():
    on_use_ability()