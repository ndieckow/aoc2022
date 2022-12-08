from collections import defaultdict
from math import prod

input = open('08.in').read().split('\n')

trees = {}
visibility = defaultdict(bool)
for y,line in enumerate(input):
    for x,c in enumerate(line):    
        trees[(x,y)] = c

def scenic_score(x,y):
    score = [0]*4
    i = 0
    height = trees[(x,y)]
    
    for xx in range(x-1,-1,-1):
        score[i] += 1
        if trees[(xx,y)] >= height:
            break
    
    i += 1
    for xx in range(x+1,len(input[0])):
        score[i] += 1
        if trees[(xx,y)] >= height:
            break
    
    i += 1
    for yy in range(y-1,-1,-1):
        score[i] += 1
        if trees[(x,yy)] >= height:
            break

    i += 1
    for yy in range(y+1,len(input)):
        score[i] += 1
        if trees[(x,yy)] >= height:
            break
    return prod(score)

ans = 0
for tree in trees:
    x,y = tree
    height = trees[tree]
    
    def update():
        global ans
        ans += 1
        visibility[(x,y)] = True

    # Left
    vis = True
    for xx in range(0,x):
        if trees[(xx,y)] >= height:
            vis = False
            break
    if vis:
        update()
        continue
    
    # Right
    vis = True
    for xx in range(x+1,len(input[0])):
        if trees[(xx,y)] >= height:
            vis = False
            break
    if vis:
        update()
        continue
    
    # Top
    vis = True
    for yy in range(0,y):
        if trees[(x,yy)] >= height:
            vis = False
            break
    if vis:
        update()
        continue
    
    # Bottom
    vis = True
    for yy in range(y+1,len(input)):
        if trees[(x,yy)] >= height:
            vis = False
            break
    if vis:
        update()
        continue

print('Part 1:',ans)

max_score = 0
for tree in trees:
    x,y = tree
    max_score = max(max_score, scenic_score(x,y))

print('Part 2:', max_score)