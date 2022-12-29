from collections import defaultdict

# This code only works for particular inputs.

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

CUBE_SIZE = 50
regions = [(0,1),(0,2),(1,1),(2,0),(2,1),(3,0)]

def r2g(rr,cc,region):
    r,c = regions[region-1]
    return (r*CUBE_SIZE + rr, c*CUBE_SIZE + cc)

def get_region(r,c):
    tmp = (r // CUBE_SIZE, c // CUBE_SIZE)
    for i,region in enumerate(regions):
        if tmp == region:
            return i+1

face_map = {
    'U' : (-1,0),
    'D' : (1,0),
    'L' : (0,-1),
    'R' : (0,1)
}
face_map_inv = {v: k for k,v in face_map.items()}

# Number the cube regions as follows:
# . 1 2
# . 3 .
# 4 5 .
# 6 . .

cubemap = {
    (1,'L'): (4,'R'), (1,'U'): (6,'R'),
    (2,'U'): (6,'U'), (2,'R'): (5,'L'), (2,'D'): (3,'L'),
    (3,'R'): (2,'U'), (3,'L'): (4,'D'),
    (4,'U'): (3,'R'), (4,'L'): (1,'R'),
    (5,'R'): (2,'L'), (5,'D'): (6,'L'),
    (6,'R'): (5,'U'), (6,'D'): (2,'D'), (6,'L'): (1,'D')
}

def next(pos,dir,part):
    r,c = pos
    dr,dc = dir
    if grid[(r+dr,c+dc)] == 0:
        if part == 1:
            if dc == -1:
                dc = max(y for (x,y) in grid if x == r and grid[(x,y)] > 0) - c
            elif dc == 1:
                dc = min(y for (x,y) in grid if x == r and grid[(x,y)] > 0) - c
            if dr == -1:
                dr = max(x for (x,y) in grid if y == c and grid[(x,y)] > 0) - r
            elif dr == 1:
                dr = min(x for (x,y) in grid if y == c and grid[(x,y)] > 0) - r
        else:
            # exploiting the fact that only one of (dr,dc) is non-zero
            bnd = 0 if dr+dc == -1 else CUBE_SIZE-1
            lr,lc = r % CUBE_SIZE, c % CUBE_SIZE
            if (abs(dr)*lr + abs(dc)*lc) == bnd:
                dir_ = face_map_inv[dir]
                reg = get_region(r,c)
                new_reg, new_dir_ = cubemap[(reg,dir_)]

                nl = nlr,nlc = 0,0 # local coordinates in the new region
                ndr,ndc = face_map[new_dir_]

                # figuring out nlr,nlc
                if ndr == 0:
                    nlc = 0 if ndc == 1 else CUBE_SIZE-1
                    if (dr,dc) == (ndr,ndc):
                        nlr = lr
                    elif (dr,dc) == (ndr,-ndc):
                        nlr = CUBE_SIZE - lr - 1
                    else:
                        nlr = lc
                else: # ndc == 0
                    nlr = 0 if ndr == 1 else CUBE_SIZE-1
                    if (dr,dc) == (ndr,ndc):
                        nlc = lc
                    elif (dr,dc) == (ndr,-ndc):
                        nlc = CUBE_SIZE - lc - 1
                    else:
                        nlc = lr
                nr,nc = r2g(nlr,nlc,new_reg)
                if (grid[(nr,nc)]) == 2:
                    return (r,c),dir
                else:
                    return (nr,nc),(ndr,ndc)
        
    if grid[(r+dr,c+dc)] == 2: # wall
        return (r,c),dir
    
    return (r+dr,c+dc),dir

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

for part in [1,2]:
    pos = (0,min(c for (r,c) in grid if r == 0 and grid[(r,c)] > 0))
    dir = (0,1)

    num = ''
    dirstr = ''

    def walk():
        global pos,num,dir
        num = int(num)
        for _ in range(num):
            prev = pos
            grid[pos] = 3 + facing(dir)
            pos,dir = next(pos,dir,part)
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
    print(f'Part {part}: {1000*(r+1) + 4*(c+1) + facing(dir)}')