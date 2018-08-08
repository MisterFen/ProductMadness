import NPCHandler
import ObjectHandler
import ScoreHandler
import Abilities

state = "title"
game_running = False

start_timer = 5000
current_timer = start_timer
time_since_last_interact = max_interact_timer = 50
time_since_last_ability = 0
max_ability_timer = 500
score_up_active = False


def on_tick():
    global current_timer, state, game_running, time_since_last_interact, time_since_last_ability, score_up_active
    current_timer -= 1
    if current_timer <= 0:
        state = "high score"
        game_running = False
    time_since_last_interact += 1
    time_since_last_ability += 1
    if score_up_active:
        if time_since_last_ability >= Abilities.score_up_duration:
            score_up_active = False
            ScoreHandler.set_score_modifier(ScoreHandler.start_score_modifier)
            print("Score up ended")


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
    Abilities.use_shout()


def use_extend_deadline():
    on_use_ability()
    Abilities.use_extend_deadline()


def use_score_up():
    on_use_ability()
    Abilities.use_score_up()
    global score_up_active
    score_up_active = True


def use_sparkle():
    on_use_ability()
