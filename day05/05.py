crates,input = open('05.in').read().split('\n\n')
crates = crates.split('\n')[::-1]
input = input.strip().split('\n')

# transpose crate input
new_crates = []
for _ in range(max([len(x) for x in crates])):
    new_crates.append('')
for line in crates:
    for i,c in enumerate(line):
        new_crates[i] += c
stacks = [list(cr.strip()[1:]) for cr in new_crates if not cr.startswith(' ')]

def solution(part):
    for line in input:
        _,amt,_,s1,_,s2 = line.split()
        amt,s1,s2 = [int(x) for x in [amt,s1,s2]]
        if part == 1:
            for _ in range(amt):
                cr = stacks[s1-1].pop()
                stacks[s2-1].append(cr)
        elif part == 2:
            tmp = []
            for _ in range(amt):
                tmp.append(stacks[s1-1].pop())
            tmp = tmp[::-1]
            stacks[s2-1] += tmp
            
    sol = ''.join([s[-1] for s in stacks])
    print(f"Part {part}: {sol}")

solution(part=1)
stacks = [list(cr.strip()[1:]) for cr in new_crates if not cr.startswith(' ')] # reset the stacks
solution(part=2)