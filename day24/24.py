from utils import *
from collections import deque,defaultdict
from math import inf

inp = open('24.in').read().split('\n')

grid = {}
for r,line in enumerate(inp):
    for c,char in enumerate(line):
        grid[(r,c)] = [] if char == '.' else [char]

bds = grid_bounds(grid)

dirmap = {
    '>' : (0,1),
    '<' : (0,-1),
    '^' : (-1,0),
    'v' : (1,0)
}

def move(grid,char,r,c,dr,dc):
    if grid[(r+dr,c+dc)] == ['#']:
        dr -= dr*(bds[1]-1)
        dc -= dc*(bds[3]-1)
    grid[(r,c)].remove(char)
    grid[(r+dr,c+dc)].append(char)

def evolve(grid):
    newgrid = {key:value[:] for key,value in grid.items()} # a lot faster than deepcopy (which isn't necessary here anyway)
    for r in range(bds[0],bds[1]+1):
        for c in range(bds[2],bds[3]+1):
            chars = grid[(r,c)]
            for char in chars:
                if char not in dirmap:
                    continue
                
                move(newgrid,char,r,c,*dirmap[char])
    return newgrid

num = (bds[1]-1)*(bds[3]-1)
gr = [grid]
for _ in range(num-1):
    gr.append(evolve(gr[-1]))

def shortest_path(start, end, t_offset=0):
    # nodes are of the form (r,c,time)
    u = (start[0],start[1],t_offset)
    Q = deque()
    Q.append(u)
    seen = {u}
    dist = defaultdict(lambda: inf)
    dist[u] = 0
    pred = {}
    while Q:
        v = Q.popleft()
        r,c,time = v
        
        if (r,c) == end:
            return time - t_offset

            # Optional: print the path
            #while v in pred:
            #    r,c,time = v
            #    v = pred[v]

            break
        for (dr,dc) in list(dirmap.values()) + [(0,0)]:
            if gr[(time+1)%num].get((r+dr,c+dc),['#']):
                continue
            w = (r+dr,c+dc,time+1)
            if w in seen:
                continue
            
            seen.add(w)
            Q.append(w)
            dist[w] = dist[v] + 1
            pred[w] = v

start = (0,1)
goal = (bds[1], bds[3]-1)

t1 = shortest_path(start, goal) # First trip
t2 = shortest_path(goal, start, t1) # Back to start
t3 = shortest_path(start, goal, t1+t2) # Back to goal

print('Part 1:', t1)
print('Part 2:', t1 + t2 + t3)