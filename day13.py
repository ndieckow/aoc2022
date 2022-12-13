import sys
import functools

sys.setrecursionlimit(10**6)

inp = open('13.in').read().split('\n\n')

def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    if x > 0:
        return 1

# Python's eval function does exactly this...
def parse(a,first):
    items = []
    last_split = 0
    level = 0
    for i,c in enumerate(a):
        if c == '[':
            level += 1
        elif c == ']':
            level -= 1
        if c == ',' and level == 0:
            items.append(a[last_split:i])
            last_split = i+1
    items.append(a[last_split:])
    out = []
    for b in items:
        if b == '[]':
            out.append([])
        elif b.startswith('['):
            out.append(parse(b[1:-1], False))
        else:
            out.append(int(b))
    return out[0] if first else out

# should not do a = [a] or b = [b], because this seems to actually change the list contents
def compare(a,b):
    if a == b:
        return 0

    if type(a) == list:
        if type(b) != list:
            return compare(a,[b])
    elif type(b) == list:
        return compare([a],b)
    else:
        return sign(b - a)

    if a == []:
        return 1
    elif b == []:
        return -1

    i = 0
    while True:
        cmp = compare(a[i],b[i])
        if cmp != 0:
            return cmp
        i += 1
        if i >= len(a):
            return 1
        elif i >= len(b):
            return -1

part1 = 0
lst = [[[2]],[[6]]]
for i,pair in enumerate(inp):
    a,b = pair.split('\n')
    arr = parse(a,True)
    brr = parse(b,True)
    lst += [arr,brr]
    if compare(arr,brr) == 1:
        part1 += (i+1)
print('Part 1:', part1)

lst = sorted(lst, key=functools.cmp_to_key(compare))
part2 = 1
for i,packet in enumerate(lst):
    if packet == [[2]] or packet == [[6]]:
        part2 *= i
print('Part 2:', part2)