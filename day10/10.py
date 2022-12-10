from collections import defaultdict

input = open('10.in').read().split('\n')

cycle = 0
X = 1

screen = defaultdict(bool)
W = 40
H = 6

dx,dy = 0,0 # drawing
part1 = 0

def print_screen():
    for y in range(H):
        row = ''
        for x in range(W):
            row += '@' if screen[(x,y)] else ' '
        print(row)

def tick():
    global cycle,dx,dy,part1
    cycle += 1
    if dx in [X-1,X,X+1]:
        screen[(dx,dy)] = True
    dx += 1
    if dx >= 40:
        dy += 1
        dx = 0
    if cycle in [20,60,100,140,180,220]:
        part1 += cycle*X

for line in input:
    tick()
    if line.startswith('addx'):
        tick()
        X += int(line.split()[1])

print('Part 1:', part1)
print('Part 2:')
print_screen()