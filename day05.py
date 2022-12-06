from collections import deque
from parse import *
import copy

input = open('input/day05input').read() 
data = input[:input.index('\n\n')].replace(' ','*').split('\n')[:-1]

# transpose state (messy)
new_list = []
for i in range(len(data[0])):
    # making a list with its index element and convert it into string.
    new_string = ''.join([ls[i] for ls in data])
    # appending the new_string int new_list
    new_list.append(new_string)

# delete [] chars
new_list = [i for i in new_list if not(any(k in i for k in '[]'))]
# remove *s
new_list = [k for k in [i.replace('*','') for i in new_list] if k != '']

Q = []
# make list of queues
for i,line in enumerate(new_list):
    Q.append(deque(line[::-1]))

# deepcopy for P2
Q2 = copy.deepcopy(Q)


# get list of instructions
times, from_, to_ = [],[],[]
for line in open('input/day05input'):
    inp = parse('move {} from {} to {}', line)
    if inp is None : continue
    times.append(int(inp[0]))
    from_.append(int(inp[1]))
    to_.append(int(inp[2]))

# part 1: remove top n from from_, and put it on top of to_ one by one
for move in range(len(times)):
    for _ in range(times[move]):
        Q[to_[move]-1].extend(Q[from_[move]-1].pop())

#part 2: remove top n from from_ and put it on top of to_ as a batch
for move2 in range(len(times)):
    crate = deque()
    for _ in range(times[move2]):
        crate.extend(Q2[from_[move2]-1].pop())
    Q2[to_[move2]-1].extend(reversed(crate))
    crate.clear()

# get top of every queue
p1 = []
p2 = []
for i in range(9):
    p1.append(Q[i][-1])
    p2.append(Q2[i][-1])

# print sol as string
print(''.join(p1),''.join(p2))
