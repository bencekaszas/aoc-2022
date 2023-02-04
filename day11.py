from parse import *
from math import prod,lcm

def make_function(i,op):
    def _(x):
        if op == '*':
            return i * x
        elif op == 'old':
            return x * x
        else:
            return x + i
    return _


state = []
monkeys = []
insp = [0,0,0,0,0,0,0,0]

for monkey in open('input/11').read().split('\n\n'):
    monkey = monkey.split('\n')
    monkey_list = list(map(int,monkey[1].split(': ')[1].split(',')))
    if '*' in monkey[2]:
        if monkey[2].split(' ')[-1] == 'old':
            op = make_function(0,'old')
        else:
            op = make_function(int(monkey[2].split(' ')[-1]),'*')
    else:
        op = make_function(int(monkey[2].split(' ')[-1]),'+')

    monkey_test = int(monkey[3].split(' ')[-1])
    monkey_to = (int(monkey[4][-1]),int(monkey[5][-1]))
    m = [op,monkey_test,monkey_to]

    monkeys.append(m)
    state.append(monkey_list)



mod = prod([monkeys[i][1] for i in range(len(monkeys))]) 



def move(m):
    for elem in state[m]:
        elem = monkeys[m][0](elem) 
        if elem % monkeys[m][1] ==  0:
            state[monkeys[m][2][0]].append(elem % mod)
        else:
            state[monkeys[m][2][1]].append(elem % mod)
        insp[m] += 1
    state[m] = []






for k in range(10000):
    print(k)
    for i,monk in enumerate(state):
        move(i)

print(prod(sorted(insp)[-2:]))

