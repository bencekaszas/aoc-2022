
rps = dict.fromkeys(['A', 'X'],1) | dict.fromkeys(['B', 'Y'], 2) | dict.fromkeys(['C', 'Z'], 3)
rps_mod = {'X' : 0, 'Y' : 3, 'Z' : 6}
rounds = [tuple(round.split(' ')) for round in open('day02input').read().split('\n')][:-2]
my_score = 0
for round in rounds:
    my_score += rps[round[1]]
    if abs(rps[round[1]] - rps[round[0]]) == 1:
        if rps[round[1]] > rps[round[0]]:
            my_score += 6
    elif rps[round[1]] == rps[round[0]]:
        my_score += 3
    else:
        if rps[round[1]] < rps[round[0]]:
            my_score += 6

my_score_mod = 0
for round in rounds:
    i = rps_mod[round[1]]
    my_score_mod += i
    if i == 0:
        if rps[round[0]] == 3:
            my_score_mod += 2
        elif rps[round[0]] == 2:
            my_score_mod += 1
        else:
            my_score_mod += 3
    elif i == 3:
        my_score_mod += rps[round[0]]
    else:
        if rps[round[0]] == 3:
            my_score_mod += 1
        elif rps[round[0]] == 2:
            my_score_mod += 3 
        else:
            my_score_mod += 2


print(my_score)
print(my_score_mod)
