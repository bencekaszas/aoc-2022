from itertools import chain

cmds = [line.strip().split(' ') for line in open('input/09test').readlines()]

#adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]



def isNear(i):
    adj_mat = list(chain.from_iterable([[(a,b) for b in range(-i,i+1)] for a in range(-i,i+1)]))
    for elem in adj_mat:
        if tuple(map(sum,zip(rope_current[0],elem))) == rope_current[i]:
                return True
    return False

head_last = (0,0)
rope_current = [(0,0) for i in range(10)]
tail_all = [(0,0)]
for cmd in cmds:
    steps = int(cmd[1])
    for i in range(steps):

        head_last = rope_current[0]

        match cmd[0]:
            case  'U':
                rope_current[0] = tuple(map(sum, zip(rope_current[0], (1,0))))
                dir = (1,0)
            case  'D':
                rope_current[0] = tuple(map(sum, zip(rope_current[0], (-1,0))))
                dir = (-1,0)
            case  'L':
                rope_current[0] = tuple(map(sum, zip(rope_current[0], (0,-1))))
                dir = (0,-1)
            case  'R':
                rope_current[0] = tuple(map(sum, zip(rope_current[0], (0,1))))
                dir = (0,1)
            case _:
                raise Exception("this shouldn't happen:(")

        for i in range(1,10):
            if not(isNear(i)): 
                print(str(i) + " NOT NEAR")
                rope_current[i] = tuple(map(sum, zip(rope_current[i], dir)))
        tail_all.append(rope_current[9])
        steps -= 1



        print(rope_current)



print(len(set(tail_all)))
