import NPCHandler
import ObjectHandler
import ScoreHandler

game_running = False

start_timer = 1000
current_timer = start_timer


def on_tick():
    global current_timer, game_running
    current_timer -= 1
    if current_timer <= 0:
        game_running = False


def on_start():
    global game_running, current_timer
    game_running = True
    current_timer = start_timer
    NPCHandler.reset()
    ObjectHandler.reset()
    ScoreHandler.reset()
