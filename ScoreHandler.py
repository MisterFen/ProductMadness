score = 0

start_score_modifier = score_modifier = 1


def increase_score(val):
    global score
    score += val * score_modifier


def reset():
    global score
    score = 0
    set_score_modifier(start_score_modifier)


def set_score_modifier(num):
    global score_modifier
    score_modifier = num
