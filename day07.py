from typing import Iterable 

dict = {}
dict_sum = {}
working_dir = ''

data = [line.strip().split(' ') for line in open('input/07').readlines()][:-1]
data[0][2] = 'root'

def get_contents(index):
    dict[working_dir] = []
    k = 1
    while k < len(data[i:]):
        if data[i+k][0] == '$': break
        else:
            dict[working_dir].append(data[i+k])
            k += 1


def flatten(items):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x

for i,line in enumerate(data):
    if line[1] == "ls":
        working_dir += data[i-1][2] + '/'
        get_contents(i)
    else:
        if line[0] == '$' and line[2] == '..':
            last_back = working_dir.rfind('/',0, len(working_dir) - 1)
            working_dir = working_dir[:last_back+1]

for dir in dict:
    for i,folder in enumerate(dict[dir]):
        if folder[0] == "dir":
            dict[dir][i] = dict[dir + folder[1] + '/']

for dir in dict:
    dict_sum[dir] = 0
    sum_ = 0
    for folder in dict[dir]:
        sum_ += sum([int(x) for x in list(flatten(folder))[::2]])
    
    dict_sum[dir] = sum_

tot = 0
for dir in dict_sum:
    if dict_sum[dir] <= 100000: tot += dict_sum[dir]

tofree = 30000000 - (70000000 - dict_sum['root/'])
candidates = []
for dir in dict_sum:
    if dict_sum[dir] >= tofree: candidates.append(dict_sum[dir])
    
print(tot)
print(sorted(candidates)[0])



