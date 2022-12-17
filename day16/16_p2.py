from collections import defaultdict
import sys
import math

sys.setrecursionlimit(1000000)

input = open('16.in').read().split('\n')

start = 'AA'

weights = {}
adj = {}
idx = {}
for i,line in enumerate(input):
    words = line.split()
    valve = words[1]
    flow_rate = int(words[4][5:-1])
    nbs = ''.join(words[9:]).split(',')
    weights[valve] = flow_rate
    adj[valve] = nbs
    idx[valve] = i

# Floyd-Warshall
dist = defaultdict(lambda: math.inf)
for i in weights:
    for j in adj[i]:
        dist[(i,j)] = 1
for i in weights:
    for j in weights:
        for k in weights:
            dist[(i,j)] = min(dist[(i,j)], dist[(i,k)] + dist[(k,j)])

mem = {}
def solve(valve,time,opened,steps=[]):
    if (valve,time,opened) in mem:
        return mem[(valve,time,opened)]
    if time == 0:
        return (0,steps)
    poss = []

    # walk to another closed valve with positive flow
    currflow = sum(weights[x] for x in weights if x in opened)
    for nb in weights:
        if nb in opened or weights[nb] == 0:
            continue
        if dist[(valve,nb)] + 1 < time:
            s1,s2 = solve(nb,time - dist[(valve,nb)] - 1, opened.union({nb}), steps+[f'walk to and open valve {nb} taking {dist[(valve,nb)] + 1} minutes'])
            val = (dist[(valve,nb)] + 1) * currflow + s1
            poss.append((val,s2))
    # last option: just wait
    poss.append((currflow*time, steps+[f'wait {time} minutes until the 30 minutes are up']))

    ans = max(poss)
    mem[(valve,time,opened)] = ans
    return ans

mem2 = {}
def solve2(valve,time,opened,part):
    if (valve,time,opened) in mem2:
        return mem2[(valve,time,opened)]
    if time == 0:
        return 0
    poss = []

    # walk to another closed valve with positive flow
    #currflow = sum(weights[x] for x in weights if x in opened)
    for nb in weights:
        if nb in opened or weights[nb] == 0:
            continue
        if dist[(valve,nb)] < time:
            s1 = solve2(nb,time - dist[(valve,nb)] - 1, opened.union({nb}), part)
            val = (time - dist[(valve,nb)] - 1) * weights[nb] + s1
            poss.append(val)
    # last option: just wait
    if part == 1:
        poss.append(0)
    else:
        poss.append(solve(start, 26, opened)[0])

    ans = max(poss)
    mem2[(valve,time,opened)] = ans
    return ans

# Part 1
#print('Part 1:', solve2(start,30,frozenset(),1))

# Part 2
print('Part 2:', solve2(start,26,frozenset(),2))
#print(mem)