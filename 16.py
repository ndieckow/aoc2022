from collections import defaultdict
import sys

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

mem = {}

def solve(valve,time,opened):
    print(time)
    tup = tuple(opened)
    if (valve,time,tup) in mem:
        return mem[(valve,time,tup)]
    if time == 0:
        return 0
    poss = []
    
    # open valve
    if not opened[idx[valve]]:
        new_opened = opened.copy()
        new_opened[idx[valve]] = 1
        poss.append(solve(valve,time-1,new_opened))
    # walk to another valve
    for nb in adj[valve]:
        poss.append(solve(nb,time-1,opened))
    
    ans = sum(weights[x] for x in weights if opened[idx[x]]) + max(poss)
    mem[(valve,time,tup)] = ans
    return ans


print(solve(start,30,[0]*len(weights)))