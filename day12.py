from collections import deque

import numpy as np

def bfs(grid, start):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        r, c = path[-1]
        if (r,c) == end:
            return path
        for r2, c2 in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
            if 0 <= r2 < R and 0 <= c2 < C and grid[r2,c2] - grid[r,c] <= 1 and (r2, c2) not in seen:
                queue.append(path + [(r2, c2)])
                seen.add((r2, c2))



inp = [line.strip() for line in open('input/12').readlines()]

R = len(inp)
C = len(inp[0])

starts = []
end = ()


grid = np.ndarray((R,C), dtype=int)

for r in range(R):
    for c in range(C):
        grid[r,c] = ord(inp[r][c])
        if grid[r,c] == ord('a'):
            starts.append((r,c))
        if grid[r,c] == ord('S'):
            starts = [(r,c)] + starts
            grid[r,c] = ord('a')
        elif grid[r,c] == ord('E'):
            end = (r,c)
            grid[r,c] = ord('z')

shortest = 1e9


for st in starts:
    curr_path = bfs(grid,st)
    if curr_path == None: continue
    elif len(curr_path)-1 < shortest:
        shortest = len(curr_path)-1

print(len(bfs(grid,starts[0]))-1)
print(shortest)
