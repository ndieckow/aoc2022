from collections import defaultdict

inp = open('18.test').read().split('\n')
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

maxx = max(x for (x,_,_) in cubes)
maxy = max(y for (_,y,_) in cubes)
maxz = max(z for (_,_,z) in cubes)

inside = set()
for z in range(0,maxz+2):
    for y in range(0,maxy+2):
        for x in range(0,maxx+2):
            if (x,y,z) not in cubes:
                inside.add((x,y,z))
total2 = -2*(maxx+2)*(maxy+2) - (maxx+2)*(maxz+2)*2 - (maxy+2)*(maxz+2)*2
total2 += count_sides(inside)
print(total2)
#print(2*total - total2)

def draw(cubes):
    for z in range(0,maxz+2):
        for y in range(0,maxy+2):
            line = ''
            for x in range(0,maxx+2):
                line += '#' if (x,y,z) in cubes else '.'
            print(line)
        input()

draw(inside)