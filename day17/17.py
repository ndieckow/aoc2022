from math import floor

inp = open('17.in').read().strip()

width = 7
rocks = set()

# y is UPWARD

def spawn(i):
    global rocks
    y = max([yy for (_,yy) in rocks] + [-1]) + 4
    if i % 5 == 0:
        x = 2
        cur = {(x,y),(x+1,y),(x+2,y),(x+3,y)}
    elif i % 5 == 1:
        y += 1
        x = 3
        cur = {(x,y),(x-1,y),(x+1,y),(x,y+1),(x,y-1)}
    elif i % 5 == 2:
        y += 1
        x = 3
        cur = {(x+1,y),(x+1,y-1),(x+1,y+1),(x-1,y-1),(x,y-1)}
    elif i % 5 == 3:
        x = 2
        cur = {(x,y),(x,y+1),(x,y+2),(x,y+3)}
    elif i % 5 == 4:
        x = 2
        cur = {(x,y),(x,y+1),(x+1,y),(x+1,y+1)}
    #rocks = rocks.union(cur)
    return cur

i = 1
j = 0
t = 0
cur = spawn(0)

def draw(ignorecur=False):
    s = [yy for (_,yy) in rocks] + [0]
    if not ignorecur:
        s += [yy for (_,yy) in cur]
    for y in range(max(s),-1,-1):
        line = ''
        for x in range(7):
            if (x,y) in rocks:
                line += '#'
            elif (x,y) in cur:
                line += '@'
            else:
                line += '.'
        print(line)

# the entire game is periodic
# after five cycles, 

for lim in [2022,1000000000000]:
    rocks = set()
    cur = spawn(0)
    i = 1
    j = 0
    t = 0

    mem = {}
    height = 0
    while i <= lim:
        jet = inp[j % len(inp)]
        if t % 2 == 0:
            move = True
            if jet == '<':
                move = all(x-1 >= 0 and (x-1,y) not in rocks for (x,y) in cur)
                if move:
                    newcur = set()
                    for (x,y) in cur:
                        newcur.add((x-1,y))
                    cur = newcur
            elif jet == '>':
                move = all(x+1 < width and (x+1,y) not in rocks for (x,y) in cur)
                if move:
                    newcur = set()
                    for (x,y) in cur:
                        newcur.add((x+1,y))
                    cur = newcur
            j += 1
        else:
            # downward
            move = all(y-1 >= 0 and (x,y-1) not in rocks for (x,y) in cur)
            if move:
                newcur = set()
                for (x,y) in cur:
                    newcur.add((x,y-1))
                cur = newcur
            else:
                rocks = rocks.union(cur)

                # have we seen this before?
                ymax = max([y for (_,y) in rocks] + [0])
                state = (i % 5, j % len(inp), frozenset((x,ymax-y) for (x,y) in rocks if ymax-y <= 20))
                if state in mem:
                    nheight,nrocks = mem[state]
                    height_diff = ymax - nheight
                    rocks_diff = i - nrocks
                    if height_diff >= 0:
                        times = floor((lim - i) / rocks_diff)
                        i += rocks_diff*times
                        height += height_diff*times
                else:
                    mem[state] = (ymax,i)

                cur = spawn(i)
                i += 1
        t += 1
    print(height + max([y for (_,y) in rocks] + [0]) + 1)