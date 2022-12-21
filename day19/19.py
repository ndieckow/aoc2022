from collections import defaultdict,Counter

blueprints = open('19.test').read().split('\n')

# number of geodes in 24 minutes
# sum up ID + no geodes for each blueprint

def get_val(dict, key):
    for c in dict:
        a,b = c
        if a == key:
            return b

for bp in blueprints:
    robots = defaultdict(list)
    #pack = Counter()
    #pack.update(['ore_robot'])

    #resources = Counter()

    words = bp.split(' ')
    id = int(words[1][:-1])
    
    robots['ore'].append(('ore', int(words[6])))

    robots['clay'].append(('ore', int(words[12])))

    robots['obsidian'].append(('ore', int(words[18])))
    robots['obsidian'].append(('clay', int(words[21])))
    
    robots['geode'].append(('ore', int(words[27])))
    robots['geode'].append(('obsidian', int(words[30])))

    t = 26
    buildable = []
    
    MEM = {}
    def solve(t, pack, resources, buildable):
        #state = (t,pack,resources,buildable)
        #if state in MEM:
        #    return MEM[state]
        def can_build(build):
            able = True
            for c in robots[build]:
                a,b = c
                if resources[a] < b:
                    able = False
                    break
            return able
        
        if t == 0:
            return resources['geode']
        for rob in pack:
            qty = pack[rob]
            if qty > 0:
                resname = rob.split('_')[0]
                resources[resname] += qty
        
        # build new robots
        ans = 0
        new_buildable = [x for x in robots if can_build(x)]
        for rob in buildable:
            if not can_build(rob):
                continue
            resources_ = resources.copy()
            for c in robots[rob]:
                a,b = c
                resources_[a] -= b
            pack_ = pack.copy()
            pack_[rob + '_robot'] += 1
            ans = max(ans, solve(t-1, pack_, resources_, new_buildable))
        ans = max(ans, solve(t-1, pack, resources, new_buildable))
        #MEM[state] = ans
        return ans
    ans= solve(26, Counter({'ore_robot' : 1}), Counter(), [])
    print(ans)
    exit()