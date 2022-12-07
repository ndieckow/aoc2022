from collections import defaultdict

input = open('07.in').read().split('\n')

files = defaultdict(list)
sizes = {}

# current directory
path = '/'

def cd(path, dir):
    if dir == '/':
        return '/'
    if dir == '..':
        return '/'.join(path.split('/')[:-1])
    return '/' + dir if path == '/' else path + '/' + dir

def total_size(path):
    if path in sizes:
        return sizes[path]
    total = 0
    for f in files[path]:
        if type(f) == tuple:
            total += f[0]
        elif type(f) == str:
            total += total_size(cd(path,f))
    sizes[path] = total
    return total

for line in input:
    s = line.split()
    if s[0] == '$':
        if s[1] == 'cd':
            path = cd(path, s[2])
        elif s[1] == 'ls':
            continue
    elif s[0] == 'dir':
        files[path].append(s[1])
    else:
        sz,fname = s
        sz = int(sz)
        files[path].append((sz,fname))

total = total_size('/')
ans = 0
for p in sizes:
    sz = sizes[p]
    if sz <= 100000:
        ans += sz
print('Part 1:', ans)

CAPACITY = 70000000
NEED = 30000000
have = CAPACITY - total
to_free = NEED - have

smallest = 100000000
stack = ['/']
while stack:
    path = stack.pop()
    smallest = min(sizes[path], smallest)
    for f in files[path]:
        if type(f) == str:
            f_path = cd(path, f)
            if sizes[f_path] < to_free:
                continue
            stack.append(f_path)
print('Part 2:', smallest)