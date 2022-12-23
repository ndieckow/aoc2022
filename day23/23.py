from collections import Counter
from copy import deepcopy

inp = open('23.in').read().split('\n')

grid = {}
for y,line in enumerate(inp):
    for x,c in enumerate(line):
        grid[(x,y)] = inp[y][x]

dirs = [(0,-1),(0,1),(-1,0),(1,0)]
dirmap = {
    (0,-1) : [(0,-1),(1,-1),(-1,-1)],
    (0,1) : [(0,1),(1,1),(-1,1)],
    (-1,0) : [(-1,0),(-1,1),(-1,-1)],
    (1,0) : [(1,0),(1,1),(1,-1)]
}
move_to = {}
moves = Counter()

def consider(x,y):
    flag = False
    nbs = set()
    for dy in range(-1,2):
        for dx in range(-1,2):
            if dy == dx == 0:
                continue
            if grid.get((x+dx,y+dy), '.') == '#':
                flag = True
                nbs.add((dx,dy))
        if flag:
            break
    if not flag:
        return
    
    for dir in dirs:
        if all(grid.get((x+dx,y+dy), '.') == '.' for (dx,dy) in dirmap[dir]):
            move_to[(x,y)] = dir
            moves[(x+dir[0],y+dir[1])] += 1
            break

for round in range(1000):
    # first half: consider
    for elf in grid:
        if grid[elf] == '#':
            c = consider(*elf)

    # second half
    new_elves = set()
    newgrid = deepcopy(grid)
    for elf in move_to:
        x,y = elf
        dx,dy = move_to[elf]
        move = True
        if moves[(x+dx,y+dy)] > 1:
            continue
        #  what if someone moved here already? this doesn't seem to change anything, but i think it should be necessary...
        newgrid[(x,y)] = '.' if (x,y) not in new_elves else '#'
        newgrid[(x+dx,y+dy)] = '#'
        new_elves.add((x+dx,y+dy))
    
    # update everything
    if grid == newgrid:
        print('Part 2:', round+1)
        break
    grid = newgrid
    move_to = {}
    moves = Counter()
    
    # swap order
    dirs = dirs[1:] + [dirs[0]]

minx = min(x for (x,y) in grid if grid[(x,y)] == '#')
maxx = max(x for (x,y) in grid if grid[(x,y)] == '#')
miny = min(y for (x,y) in grid if grid[(x,y)] == '#')
maxy = max(y for (x,y) in grid if grid[(x,y)] == '#')

ans = 0
for x in range(minx,maxx+1):
    for y in range(miny,maxy+1):
        ans += 1 if grid.get((x,y),'.') == '.' else 0
print(ans)