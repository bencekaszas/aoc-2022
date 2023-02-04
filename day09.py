from math import prod

cmds = [line.strip().split(' ') for line in open('input/09').readlines()]

adj = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

rope_current = [(0,0) for _ in range(9)]
end_all = [(0,0)]

def isNear(elem,i):
    for ad in adj:
        if tup_add(rope_current[i-1],ad) == elem:
            return True
    
    return False
def move(b,a):
    for adj in [(2,0),(-2,0),(0,2),(0,-2)]:
        if tup_add(b,adj) == a:
            if adj == (2,0):
                return (1,0)
            if adj == (-2,0):
                return (-1,0)
            if adj == (0,2):
                return (0,1)
            if adj == (0,-2):
                return (0,-1)

    for adj in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2),(2,2),(2,-2),(-2,2),(-2,-2)]:
        if tup_add(b,adj) == a:
            if adj == (2,1) or adj == (1,2) or adj == (2,2):
                return (1,1)
            if adj == (-2,1) or adj == (-1,2)or adj == (-2,2):
                return (-1,1)
            if adj == (-2,-1) or adj == (-1,-2)or adj == (-2,-2):
                return (-1,-1)
            if adj == (2,-1) or adj == (1,-2)or adj == (2,-2):
                return (1,-1)

    raise Exception ('wtf', b, a)


def tup_add(a,b):
    return tuple(map(sum,zip(a,b)))
            

head_last = (0,0)
tail_all = [(0,0)]
'''
for cmd in cmds:
    steps = int(cmd[1])
    for i in range(steps):
        head_last = head_current

        match cmd[0]:
            case  'U':
                head_current = tuple(map(sum, zip(head_current, (1,0))))
            case  'D':
                head_current = tuple(map(sum, zip(head_current, (-1,0))))
            case  'L':
                head_current = tuple(map(sum, zip(head_current, (0,-1))))
            case  'R':
                head_current = tuple(map(sum, zip(head_current, (0,1))))
            case _:
                raise Exception("this shouldn't happen:(")
        
        if isNear():
            steps -= 1
        else:
            tail_all.append(head_last)
            steps -= 1
'''      



for cmd in cmds:
    steps = int(cmd[1])
    for i in range(steps):
        head_last = rope_current[0]

        match cmd[0]:
            case  'U':
                dir = (1,0)
                rope_current[0] = tup_add(rope_current[0],(1,0))
            case  'D':
                dir = (-1,0)
                rope_current[0] = tup_add(rope_current[0],(-1,0))
            case  'L':
                dir = (0,-1)
                rope_current[0] = tup_add(rope_current[0],(0,-1))
            case  'R':
                dir = (0,1)
                rope_current[0] = tup_add(rope_current[0],(0,1))
            case _:
                raise Exception("move not permitted; this shouldn't happen:(")
        
        for k in range(1,9):
            if not(isNear(rope_current[k],k)):
                rope_current[k] = tup_add(move(rope_current[k],rope_current[k-1]),rope_current[k])
        if not(isNear(end_all[-1],9)):
            end_all.append(tup_add(move(end_all[-1],rope_current[8]),end_all[-1]))
        if not(isNear(tail_all[-1],1)):
            tail_all.append(head_last)

print(len(set(tail_all)))
print(len(set(end_all)))
