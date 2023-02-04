from math import prod

cmds = [line.strip().split(' ') for line in open('input/10').readlines()]

tick = [1 for _ in range(300)]
t = 0

for cmd in cmds:
    if cmd[0] == "noop":
        tick[t+1] = tick[t]
        t += 1
    else:
        tick[t: t+ 3] = [tick[t] for _ in tick[t :t + 3]]
        tick[t+2] += int(cmd[1])
        t += 2


print(sum(list(map(prod, zip(tick[19::40][:6],[x for x in range(20,221,40)])))))


R = 6
C = 40


for r in range(R):
    row = ''
    for c in range(C):
        ind = r*40+c
        if c  == tick[ind]-1 or c  == tick[ind] or c  == tick[ind]+1:
            row += '#'
        else:
            row += '.'
    print(row)




