inp = open('21.in').read().split('\n')

jobs = {}

for line in inp:
    words = line.split()
    monkey = words[0][:-1]
    if len(words) == 2:
        jobs[monkey] = int(words[1])
    else:
        left = words[1]
        op = words[2]
        right = words[3]
        jobs[monkey] = (op,left,right)

def eval(exp):
    if type(exp) == int:
        return exp
    op,left,right = exp
    left = eval(jobs[left])
    right = eval(jobs[right])
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        return left // right
    elif op == '=':
        return (left, right)

print('Part 1:', eval(jobs['root']))

# Figured this out per hand by just playing around and eventually noticing that, if the number starts with certain 4 digits,
# that are as close to the desired number as possible, the remaining digits only decreased (or increased, I forgot already) the number.
print('Part 2:', 3740214169961)