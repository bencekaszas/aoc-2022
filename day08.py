import numpy as np

grid =  np.array([[int(y) for y in x] for x in open('input/08').read().strip().split()])

R = len(grid)
C = len(grid[0])




seeable = 0
for r,row in enumerate(grid):
    for c,col in enumerate(row):
        if len(grid[:r,c]) == 0 or len(grid[r+1:,c]) == 0 or len(grid[r,:c]) == 0 or len(grid[r,c+1:]) == 0:
            seeable += 1
            continue
        if max(grid[:r,c]) < grid[r,c]:
            seeable += 1
            continue
        elif max(grid[r+1:,c]) < grid[r,c]:
            seeable += 1
            continue
        elif max(grid[r,:c]) < grid[r,c]:
            seeable += 1
            continue
        elif max(grid[r,c+1:]) < grid[r,c]:
            seeable += 1
            continue


scenic = np.zeros_like(grid) 
print(scenic)

for r,row in enumerate(grid):
    for c,col in enumerate(row):
        up,down,left,right = 1,1,1,1
        if  r-up > 0:
            while grid[r,c] > grid[r-up,c] and r-up > 0:
                up += 1
        if r + down < R:
            while grid[r,c] > grid[r+down,c] and r + down < R -1:
                down += 1
        if c-left > 0:
            while grid[r,c] > grid[r,c-left] and c-left > 0:
                left +=  1
        if c + right< C:
            while grid[r,c] > grid[r,c+right] and c + right < C -1:
                right += 1
        scenic[r,c] = up*down*left*right


        if len(grid[:r,c]) == 0 or len(grid[r+1:,c]) == 0 or len(grid[r,:c]) == 0 or len(grid[r,c+1:]) == 0:
            scenic[r,c] = 0



print(max([max(row) for row in scenic]))

#print(seeable)
