import sys
import os
import math

sys.path.append(os.path.join(sys.path[0], '..')) # also look in the parent directory

from collections import defaultdict
from utils import memoize

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
def solve(valve,time,opened):
    if (valve,time,opened) in mem:
        return mem[(valve,time,opened)]
    if time == 0:
        return 0
    poss = []

    # walk to another closed valve with positive flow
    currflow = sum(weights[x] for x in weights if x in opened)
    for nb in weights:
        if nb in opened or weights[nb] == 0:
            continue
        dur = dist[(valve,nb)] + 1
        if dur <= time:
            val = dur * currflow + solve(nb, time - dur, opened.union({nb}))
            poss.append(val)
    # last option: just wait until the time runs out
    poss.append(currflow * time)

    ans = max(poss)
    mem[(valve,time,opened)] = ans
    return ans

# This DP is addition based.
# Given state (valve,time,opened), it returns how much ADDITIONAL flow can be obtained.
# In the initial state, both DPs of course return the same.
mem2 = {}
def solve2(valve,time,opened,part):
    state = (valve,time,opened,part)
    if state in mem2:
        return mem2[state]
    if time == 0:
        return 0 if part == 1 else solve2(start, 26, opened, 1)
    poss = []

    # walk to another closed valve with positive flow
    for nb in weights:
        if nb in opened or weights[nb] == 0:
            continue
        dur = dist[(valve,nb)] + 1
        if dur <= time:
            val = (time - dur) * weights[nb] + solve2(nb, time - dur, opened.union({nb}), part)
            poss.append(val)
    
    if part == 1:
        poss.append(0) # just wait
    else:
        poss.append(solve2(start, 26, opened, 1)) # let the elephant do the rest

    ans = max(poss)
    mem2[state] = ans
    return ans

# Part 1
#print('Part 1:', solve2(start,30,frozenset(),1))

# 2249 too low; 2384 wrong

print('Part 1:', solve2(start,30,frozenset(),1))
mem2 = {}
print('Part 2:', solve2(start,26,frozenset(),2))