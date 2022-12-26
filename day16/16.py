from collections import defaultdict

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
def solve(valve,time,opened,part):
    state = (valve,time,opened,part)
    if state in mem:
        return mem[state]
    if time == 0:
        return 0 if part == 1 else solve(start, 26, opened, 1)
    poss = []
    
    # open valve
    if valve not in opened and weights[valve] > 0:
        poss.append((time-1)*weights[valve] + solve(valve, time-1, opened.union({valve}), part))
    # walk to another valve
    for nb in adj[valve]:
        poss.append(solve(nb, time-1, opened, part))
    
    ans = max(poss)
    mem[state] = ans
    return ans

print('Part 1:', solve(start,30,frozenset(), 1))
print('Part 2:', solve(start,26,frozenset(), 2))