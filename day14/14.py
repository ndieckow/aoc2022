from collections import defaultdict
from copy import deepcopy

inp = open('14.in').read().split('\n')

# 1 = rock
# 2 = sand
rocks = defaultdict(int)

sand = (0,500)

for line in inp:
    pairs = line.split(' -> ')
    for i,pair in enumerate(pairs[:-1]):
        c1,r1 = [int(x) for x in pair.split(',')]
        c2,r2 = [int(x) for x in pairs[i+1].split(',')]
        step_r = -1 if r2 < r1 else 1
        step_c = -1 if c2 < c1 else 1
        for rr in range(r1,r2+step_r,step_r):
            for cc in range(c1,c2+step_c,step_c):
                rocks[(rr,cc)] = 1

minR = min([r for (r,_) in rocks])
minC = min([c for (_,c) in rocks])
R = max([r for (r,_) in rocks])
C = max([c for (_,c) in rocks])

def draw():
    for r in range(minR,R+1):
        line = ''
        for c in range(minC,C+1):
            ch = rocks[(r,c)]
            if ch == 1:
                line += '#'
            elif ch == 2:
                line += 'o'
            else:
                line += '.'
        print(line)

rocks_ = deepcopy(rocks)
for part in [1,2]:
    rocks = deepcopy(rocks_)
    corn = sand
    i = 0
    units = 1
    while True:
        i += 1
        new_corn = False
        r,c = corn
        if r+1 == R+2:
            new_corn = True
        elif rocks[(r+1,c)] == 0:
            corn = (r+1,c)
        elif rocks[(r+1,c-1)] == 0:
            corn = (r+1,c-1)
        elif rocks[(r+1,c+1)] == 0:
            corn = (r+1,c+1)
        else:
            new_corn = True
        if new_corn:
            if part == 2 and corn[0] == 0:
                print('Part 2:', units)
                break
            corn = sand
            units += 1
        else:
            rocks[(r,c)] = 0
            rocks[corn] = 2
            if part == 1 and corn[0] > R:
                print('Part 1:', units-1)
                break
#draw()