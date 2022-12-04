input = open("04.in").read().strip().split('\n')

ans1 = 0
ans2 = 0
for line in input:
    a,b = line.split(',')
    c,d = [int(x) for x in a.split('-')]
    e,f = [int(x) for x in b.split('-')]
    if c <= e and d >= f or e <= c and f >= d:
        ans1 += 1
        ans2 += 1
    if e < c <= f < d or c < e <= d < f:
        ans2 += 1

print("Part 1:", ans1)
print("Part 2:", ans2)