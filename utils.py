def memoize(f):
    mem = {}
    def F(*x):
        if x in mem:
            return mem[x]
        val = f(*x)
        mem[x] = val
        return val
    return F

# does it work with defaultdict?
def grid_bounds(grid, pred=lambda x: True):
    min_r = min(r for (r,c) in grid if pred(grid[(r,c)]))
    max_r = max(r for (r,c) in grid if pred(grid[(r,c)]))
    min_c = min(c for (r,c) in grid if pred(grid[(r,c)]))
    max_c = max(c for (r,c) in grid if pred(grid[(r,c)]))
    return min_r,max_r,min_c,max_c

def print_grid(grid):
    bds = grid_bounds(grid)
    for r in range(bds[0],bds[1]+1):
        line = ''
        for c in range(bds[2],bds[3]+1):
            line += grid[(r,c)]
        print(line)
    print('\n')