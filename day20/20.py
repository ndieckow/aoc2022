from collections import Counter

coords = [int(x) for x in open('20.in').read().split('\n')]
N = len(coords)

class dll:
    
    def __init__(self,value,next,prev):
        self.value = value
        self.next = next
        self.prev = prev

    def __iter__(self):
        return self.value
    
    def __next__(self):
        return self.next

def print_dll(ls,num=N):
    cur = ls
    line = '< '
    for i in range(num):
        line += str(cur.value)
        line += ', ' if i < num-1 else ''
        cur = cur.next
    line += ' >'
    print(line)

def list_to_dll(ls):
    start = dll(ls[0],None,None)
    prev = start
    cur = None
    for i in range(1,len(ls)):
        cur = dll(ls[i],None,prev)
        prev.next = cur
        prev = cur
    prev.next = start
    start.prev = prev
    return start

def shift(node,j):
    if j == 0:
        return

    after = node
    if j > 0:
        while j > 0:
            after = after.next
            if after == node:
                after = after.next
            j -= 1
    elif j < 0:
        while j < 1: # < 1 instead of 0 because we append to the right
            after = after.prev
            if after == node:
                after = after.prev
            j += 1
    
    node.next.prev = node.prev
    node.prev.next = node.next
    node.prev = after
    node.next = after.next
    after.next.prev = node
    after.next = node


for part in [1,2]:
    if part == 2:
        coords = [811589153*x for x in coords]
    
    d = list_to_dll(coords)
    dlls = {}
    cur = d
    ctr = Counter()
    newcoords = []
    for c in coords:
        tup = (c,ctr[c])
        newcoords.append(tup)
        dlls[tup] = cur
        ctr[c] += 1
        cur = cur.next

    for _ in range(10 if part == 2 else 1):
        for c in newcoords:
            shift(dlls[c], c[0] % (N-1))

    ans = 0
    cur = dlls[(0,0)]

    for i in range(3001):
        if i % 1000 == 0:
            ans += cur.value
        cur = cur.next
    print(f'Part {part}: {ans}')