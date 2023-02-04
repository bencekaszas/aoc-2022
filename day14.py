import numpy as np
#import matplotlib.pyplot as plt

inp = open('input/14').read().strip().split('\n')

setdown = True
def move(index,start):
    global setdown

    if grid[1,500-offset[1]] != 0:
        if grid[1,500-offset[1]-1] != 0:
            if grid[1,500-offset[1]+1] != 0:
                print('HEYY')
                setdown = False

    '''
    if start >= x_max -1:
        setdown = False
        return 
    '''
    i = start
    while grid[i,index] == 0:
        i += 1
        '''
        if i == x_max:
            setdown = False
            return 
        '''
    else:
        #print(i)
        if grid[i,index-1] != 0:
            if grid[i,index+1] != 0:
                grid[i-1,index] = 2
                return
            else:
                move(index+1,i)
        else:
            move(index-1,i)
        


x_ = []
y_ = []
coords = []
for line in inp:
    line = line.split(' -> ')
    coord = [(int(co.split(',')[0]),int(co.split(',')[1])) for co in line]
    coords.append(coord)
    for (y,x) in coord:
        x_.append(x)
        y_.append(y)

offset = (0,min(y_)-250)

x_max = max(x_)-min(x_)+17
y_max = max(y_)-min(y_)+500

grid = np.zeros((x_max,y_max),dtype=int)

for l in range(len(inp)):
    for i,(a,b) in enumerate(coords[l]):
        y,x = a-offset[1],b-offset[0]
        if i+1 < len(coords[l]):
            if coords[l][i+1][0] == a:
                for index in range(abs(coords[l][i+1][1]-b)+1):
                    if b < coords[l][i+1][1]:
                        grid[x+index,y] = 1
                    else:
                        grid[x-index,y] = 1
                    
            else:
                for index in range(abs(coords[l][i+1][0]-a)+1):
                    if a < coords[l][i+1][0]:
                        grid[x,y+index] = 1
                    else:
                        grid[x,y-index] = 1
                    

grid[x_max-2,:] = [1 for _ in range(y_max)]


for r in range(x_max):
    row = ''
    for c in range(y_max):
        if r == 0 and c == (500-offset[1]):
            row += '+'
        elif grid[r,c] == 1:
            row += '#'
        else:
            row += '.'
    print(row)

s = 0



while setdown:
    move(500 - offset[1],0)

print()
for r in range(x_max):
    row = ''
    for c in range(y_max):
        if r == 0 and c == (500-offset[1]):
            row += '+'
        elif grid[r,c] == 1:
            row += '#'
        elif grid[r,c] == 2:
            row += 'o'
            s += 1    
        else:
            row += '.'
    print(row)
print(s+1)




