from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

input = open('16.test').read().split('\n')

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
    #print(mem)
    if (valve,time,opened) in mem:
        return mem[(valve,time,opened)]
    if time == 0:
        return 0
    poss = []
    
    #ivalve = idx[valve]
    # open valve
    if not valve in opened and weights[valve] > 0:
        poss.append(solve(valve,time-1,opened.union({valve})))
    # walk to another valve
    for nb in adj[valve]:
        poss.append(solve(nb,time-1,opened))
    
    ans = sum(weights[x] for x in weights if x in opened) + max(poss)
    mem[(valve,time,opened)] = ans
    return ans

print(solve(start,30,frozenset()))

# Go through all possible bipartitions
# For each bipartition (A,B), let protag do A and elephant do B
# use Floyd-Warshall to compute distances