from collections import defaultdict

inp = open('09.in').read().split('\n')

# tail follows diagonally, if not in same row&col
# tail follows hor/vert, if in same row OR col

def sgn(a):
    return int(abs(a)/a)

class Entity():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def move(self,dir,amt):
        if dir == 'R':
            self.x += amt
        elif dir == 'L':
            self.x -= amt
        elif dir == 'U':
            self.y -= amt
        elif dir == 'D':
            self.y += amt

def solve(n_knots):
    tpos = defaultdict(bool)
    knots = [Entity(0,0) for _ in range(n_knots)]

    for line in inp:
        a,b = line.split()
        b = int(b)
        while b > 0:
            knots[0].move(a,1)
            for i,knot in enumerate(knots[:-1]):
                if abs(knot.x - knots[i+1].x) <= 1 and abs(knot.y - knots[i+1].y) <= 1: # touching
                    pass
                elif knot.x == knots[i+1].x:
                    knots[i+1].y += sgn(knot.y - knots[i+1].y)
                elif knot.y == knots[i+1].y:
                    knots[i+1].x += sgn(knot.x - knots[i+1].x)
                else:
                    knots[i+1].x += sgn(knot.x - knots[i+1].x)
                    knots[i+1].y += sgn(knot.y - knots[i+1].y)
                if i == len(knots)-2:
                    tpos[(knots[i+1].x,knots[i+1].y)] = True
            b -= 1
    return len(tpos)

print('Part 1:', solve(2))
print('Part 2:', solve(10))