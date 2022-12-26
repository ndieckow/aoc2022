import sys

sys.setrecursionlimit(10000)

blueprints = open('19.in').read().split('\n')

# Warning: Part 2 is extremely slow

def leq(a,b):
    assert(len(a) == len(b))
    for i in range(len(a)):
        if a[i] > b[i]:
            return False
    return True

def sub(a,b):
    assert(len(a) == len(b))
    return tuple(a[i] - b[i] for i in range(len(a)))

def add(a,b):
    assert(len(a) == len(b))
    return tuple(a[i] + b[i] for i in range(len(a)))

def solu(part):
    ans = 0 if part == 1 else 1
    for i,bp in enumerate(blueprints):
        if part == 2 and i > 2:
            return ans
        
        words = bp.split(' ')
        id = int(words[1][:-1])
        
        recipe = [
            (int(words[6]), 0, 0, 0),
            (int(words[12]), 0, 0, 0),
            (int(words[18]), int(words[21]), 0, 0),
            (int(words[27]), 0, int(words[30]), 0),
            (0, 0, 0, 0) # build no robot
        ]

        T = 24 if part == 1 else 32
        init = (0,0,0,0,1,0,0,0,T)

        # Problem: huge state space (5^24)
        # Potential solution: use common sense to build some heuristics such as
        # * if you can build a geode robot, build a geode robot
        # * same with obsidian robots; this actually helps a lot

        mem = {}
        def solve(ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time):
            state = (ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time)
            if state in mem:
                return mem[state]
            
            if time == 0:
                return geode
            
            poss = []

            def do_the_thing(i):
                rec = recipe[i]
                if leq(rec, state[:4]):
                    tmp = sub(state[:4], rec) # used-up resources
                    tmp = add(tmp, state[4:-1]) # harvested resources
                    tmp = list(tmp + state[4:])

                    if i < 4:
                        tmp[4+i] += 1 # new robot
                    tmp[-1] -= 1 # one minute passed
                    poss.append(solve(*tmp))

            # if you can, build a geode robot
            if leq(recipe[3], state[:4]):
                do_the_thing(3)
            elif leq(recipe[2], state[:4]): # or an obsidian robot
                do_the_thing(2)
            else:
                for i,rec in enumerate(recipe):
                    do_the_thing(i)
            ans = max(poss)
            mem[state] = ans
            return ans
        
        slv = solve(*init)
        if part == 1:
            ans += id * slv
        else:
            ans *= slv
    return ans

print('Part 1:', solu(1))
print('Part 2:', solu(2))