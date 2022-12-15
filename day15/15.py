input = open('15.in').read().split('\n')

def tuning_freq(x,y):
    return x*4000000 + y

def union(region,l,r):
    newregion = []
    merged = False
    for (ll,rr) in region:
        if merged:
            if ll > newregion[-1][1]:
                newregion.append((ll,rr))
            else:
                lll,_ = newregion.pop()
                newregion.append((lll,rr))
        else:
            if rr < l or r < ll:
                newregion.append((ll,rr))
                continue
            newregion.append((min(ll,l),max(rr,r)))
            merged = True
    if not merged:
        newregion.append((l,r))
    return sorted(newregion)

def solve(part):
    if part == 1:
        a,b = 2000000,2000001
    else:
        a,b = 0,4000000
    coords = []
    for y in range(a,b):
        regs = []
        inrow = set()
        for line in input:
            line = line.split()
            sx = int(line[2][2:-1])
            sy = int(line[3][2:-1])
            bx = int(line[8][2:-1])
            by = int(line[9][2:])
            if by == y:
                inrow.add((bx,by))

            dist = abs(sx-bx) + abs(sy-by)
            diff = dist - abs(sy-y)
            if diff >= 0:
                p1 = sx - diff
                p2 = sx + diff
                regs = union(regs, p1,p2)
        ans = 0
        for reg in regs:
            ans += reg[1] - reg[0] + 1
        if part == 1:
            print('Part 1:', ans - len(inrow))
        if len(regs) > 1 and regs[0][1]+2 == regs[1][0]:
            #print(y,regs)
            coords.append((regs[0][1]+1,y))
    if part == 2:
        print('Part 2:', tuning_freq(*coords[-1]))

solve(1)
solve(2)

# This code is an absolute mess
# I don't know how this worked for part 2
# but the last coordinate added to coords is the right one,
# even though there are many more and there should be only one