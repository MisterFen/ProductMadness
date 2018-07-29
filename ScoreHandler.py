score = 0

score_modifier = 1


def increase_score(val):
    global score
    score += val * score_modifier
    print('Increased score: ' + str(score))
