input = open("01.in").read().split('\n')

most = 0
elf = 0
list = []
for x in input:
    if x == '':
        most = max(most,elf)
        list.append(elf)
        elf = 0
        continue
    elf += int(x)

print('Part 1:', most)
print('Part 2:', sum(sorted(list)[::-1][:3]))