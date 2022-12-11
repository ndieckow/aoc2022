from math import prod
from copy import deepcopy

inp = open('11.in').read().split('\n\n')

N = len(inp)
init_queues = []
funcs = []
test = []
test_true = []
test_false = []

for block in inp:
    lines = block.split('\n')
    id = int(lines[0][:-1].split()[-1])
    init_queues.append([int(x) for x in lines[1].strip().replace(',', '').split()[2:]])
    funcs.append(' '.join(lines[2].split()[3:]))
    test.append(int(lines[3].split()[-1]))
    test_true.append(int(lines[4].split()[-1]))
    test_false.append(int(lines[5].split()[-1]))

mod = prod(test)

def solve(part):
    count = [0]*N
    queues = deepcopy(init_queues)
    R = 20 if part == 1 else 10000
    for _ in range(R):
        for i in range(N):
            for item in queues[i]:
                # inspect
                old = item
                item = eval(funcs[i])
                count[i] += 1
                # relief (or not)
                if part == 1:
                    item //= 3
                # Why does this work?
                # If item = a*mod + b, then item is divisible by a number in `test` if and only if b is divisible by that number.
                # This is because a*mod is disivible by all numbers in `test` (by construction), so b is the "gatekeeper" for divisibility.
                # Hence, we can just consider b because the divisibility relations are preserved.
                item %= mod
                # test
                if item % test[i] == 0:
                    queues[test_true[i]].append(item)
                else:
                    queues[test_false[i]].append(item)
            queues[i] = []
    return prod(sorted(count)[-2:])

print('Part 1:', solve(1))
print('Part 2:', solve(2))