from collections import deque,defaultdict

inp = open('18.in').read().split('\n')
cubes = [tuple(int(x) for x in line.split(',')) for line in inp]

def count_sides(cubes):
    total = len(cubes)*6
    for c1 in cubes:
        for c2 in cubes:
            x1,y1,z1 = c1
            x2,y2,z2 = c2
            if abs(x1-x2)+abs(y1-y2)+abs(z1-z2) == 1:
                total -= 1
    return total
total = count_sides(cubes)
print('Part 1:', total)

def bfs(start):
    Q = deque([start])
    seen = set()
    graph = defaultdict(set)
    while Q:
        v = Q.popleft()
        x,y,z = v

        # check if we exited the bounding box
        if not (0 <= x <= maxx and 0 <= y <= maxy and 0 <= z <= maxz):
            return {a:[0]*6 for a in seen}

        # initialize dict entry
        graph[v]

        for (dx,dy,dz) in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            w = (x+dx,y+dy,z+dz)
            if w in cubes:
                continue
            graph[v].add(w)
            graph[w].add(v)
            if w in seen:
                continue
            seen.add(w)
            Q.append(w)
    return graph

maxx = max(x for (x,_,_) in cubes)
maxy = max(y for (_,y,_) in cubes)
maxz = max(z for (_,_,z) in cubes)

# Idea: Try and flood (using BFS) every voxel that is not occupied by a cube.
# Then use the number of neighbors for each unoccupied voxel in this connected region to lower the total number of sides.

flooded = set()
for z in range(0,maxz+1):
    for y in range(0,maxy+1):
        for x in range(0,maxx+1):
            v = (x,y,z)
            if v in cubes or v in flooded:
                continue
            graph = bfs(v)
            #print(graph)
            flooded |= set(graph.keys())
            total -= len(graph)*6 - sum(len(graph[u]) for u in graph)
print('Part 2:', total)

def debug_draw():
    for z in range(0,maxz+1):
        for y in range(0,maxy+1):
            line = ''
            for x in range(0,maxx+1):
                line += '#' if (x,y,z) in cubes else '.'
            print(line)
        input()