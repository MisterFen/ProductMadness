import NPCHandler
import ObjectHandler
import ScoreHandler
import Abilities
import SparkleHandler

state = "title"
game_running = False

start_timer = 5000
current_timer = start_timer
time_since_last_interact = max_interact_timer = 50
time_since_last_ability = 0
max_ability_timer = 500
score_up_active = False
sparkle_active = False
last_shout = 500


def on_tick():
    global current_timer, state, game_running, time_since_last_interact, time_since_last_ability, score_up_active, sparkle_active, last_shout
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
    if sparkle_active:
        if SparkleHandler.timer > 0:
            sparkle_active = True
            SparkleHandler.timer -= 1
        else:
            sparkle_active = False
    last_shout += 1

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


def use_shout(x, y):
    on_use_ability()
    Abilities.use_shout(x, y)


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
    Abilities.use_sparkle()
    global sparkle_active
    sparkle_active = True


def abilities_ready_to_use():
    if time_since_last_ability >= max_ability_timer:
        return True
    else:
        return False