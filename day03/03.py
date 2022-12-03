input = open("03.in").read().strip().split('\n')

def prio(c):
    return ord(c) - ord('a') + 1 if ord(c) > ord('Z') else ord(c) - ord('A') + 27

ans = 0
for line in input:
    n = len(line) // 2
    first = line[:n]
    last = line[n:]
    double = set()
    for c in last:
        if c in first:
            double.add(c)
    ans += sum(prio(x) for x in double)
print('Part 1:', ans)

# Part 2
ans2 = 0
i = 0
while i < len(input):
    aa,bb,cc = input[i],input[i+1],input[i+2]
    common = set()
    for c in aa:
        if c in bb and c in cc:
            common.add(c)
    if len(common) == 1:
        ans2 += sum(prio(x) for x in common)
    i += 3
print('Part 2', ans2)