from collections import defaultdict

inp = open('22.in').read().split('\n')
path = inp[-1]
karte = inp[:-2]

# 0 = empty, 1 = walkable, 2 = wall
grid = defaultdict(int)
for r in range(len(karte)):
    for c in range(len(karte[0])):
        if c >= len(karte[r]):
            grid[(r,c)] = 0
            continue
        v = karte[r][c]
        if v == ' ':
            grid[(r,c)] = 0
        elif v == '.':
            grid[(r,c)] = 1
        elif v == '#':
            grid[(r,c)] = 2

def facing(dir):
    r,c = dir
    return abs(2 * r + c - 1)

def turn(dir,turn):
    dr,dc = dir
    return (-dc,dr) if turn == 'L' else (dc,-dr)

# Number the cube regions as follows:
# . 1 2
# . 3 .
# 4 5 .
# 6 . .
#
# Weird transitions:
# 1, facing left: 4 
# 1, facing up:   6 facing right, left becomes up

def next(pos,dir,part):
    r,c = pos
    dr,dc = dir
    if part == 1:
        if grid[(r+dr,c+dc)] == 0:
            if dc == -1:
                dc = max(y for (x,y) in grid if x == r and grid[(x,y)] > 0) - c
            elif dc == 1:
                dc = min(y for (x,y) in grid if x == r and grid[(x,y)] > 0) - c
            if dr == -1:
                dr = max(x for (x,y) in grid if y == c and grid[(x,y)] > 0) - r
            elif dr == 1:
                dr = min(x for (x,y) in grid if y == c and grid[(x,y)] > 0) - r
        if grid[(r+dr,c+dc)] == 2: # wall
            return (r,c)
    else:
        pass
    return (r+dr,c+dc)

drawmap = {
    0 : ' ',
    1 : '.',
    2 : '#',
    3 : '>',
    4 : 'v',
    5 : '<',
    6 : '^'
}

def draw():
    out = ''
    for r in range(max(r for (r,_) in grid)+1):
        for c in range(max(c for (_,c) in grid)+1):
            v = grid[(r,c)]
            out += drawmap[v]
        out += '\n'
    return out

pos = (0,min(c for (r,c) in grid if r == 0 and grid[(r,c)] > 0))
dir = (0,1)

num = ''
dirstr = ''
part = 2

def walk():
    global pos,num
    num = int(num)
    for _ in range(num):
        prev = pos
        grid[pos] = 3 + facing(dir)
        pos = next(pos,dir,part)
        if pos == prev:
            break

for c in path:
    if c in ['L','R']:
        walk()
        dirstr = c
        dir = turn(dir,dirstr)
        num = ''
        grid[pos] = 3 + facing(dir)
        continue
    num += c
# walk the last steps
walk()

r,c = pos
print(1000*(r+1) + 4*(c+1) + facing(dir))