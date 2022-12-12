from collections import defaultdict,deque
import math

input = open('12.in').read().split('\n')

R,C = len(input),len(input[0])
grid = [[0]*len(input[0]) for _ in range(len(input))]

for r,row in enumerate(input):
    for c,ch in enumerate(row):
        if ch == 'S':
            start = (r,c)
            ch = 'a'
        elif ch == 'E':
            dest = (r,c)
            ch = 'z'
        grid[r][c] = ord(ch) - ord('a') + 1

def solve(part):
    dist = defaultdict(lambda: math.inf)
    dist[start] = 0
    seen = set()
    q = deque()
    for r in range(R):
        for c in range(C):
            if (r,c) == start and part == 1 or grid[r][c] == 1 and part == 2:
                q.append(((r,c),0))
    while q:
        (r,c),d = q.popleft()
        if (r,c) in seen:
            continue
        seen.add((r,c))
        if (r,c) == dest:
            return d
        for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            if r+dr < 0 or r+dr >= len(input) or c+dc < 0 or c+dc >= len(input[0]):
                continue
            if grid[r+dr][c+dc] - grid[r][c] <= 1:
                q.append(((r+dr,c+dc),d+1))

print('Part 1:', solve(1))
print('Part 2:', solve(2))