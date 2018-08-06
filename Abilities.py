import GameLogic
import random


def use_extend_deadline():
    random.seed()
    max_deadline_increase = 200
    remaining_time_percentage = 1-(GameLogic.current_timer / GameLogic.start_timer)
    amount_to_increase = int(remaining_time_percentage * max_deadline_increase)
    amount_to_increase += random.randint(3, 30)
    GameLogic.current_timer += amount_to_increase
    print('Increased by: '+str(amount_to_increase))