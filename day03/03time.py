import time

input = open("03.in").read().strip().split('\n')

# Needs to be around 20 or above for the intersection approach to be faster. Better time complexity does not always mean a faster algorithm!
# Setting it to, say, 2000, really highlights the difference. On my laptop, the naive approach takes around 7.5 seconds, while the
# intersection method takes just 0.1 seconds.
factor = 20

def prio(c):
    return ord(c) - ord('a') + 1 if ord(c) > ord('Z') else ord(c) - ord('A') + 27

def compute(way = 'naive'):
    ans = 0
    i = 0
    while i < len(input):
        aa,bb,cc = input[i]*factor,input[i+1]*factor,input[i+2]*factor
        if way == 'naive':
            common = set()
            for c in aa:
                if c in bb and c in cc:
                    common.add(c)
        elif way == 'intersection':
            common = set(aa).intersection(set(bb)).intersection(set(cc))
        if len(common) == 1:
            ans += sum(prio(x) for x in common)
        i += 3
    print(ans)

start = time.time()
compute('naive')
print("Time (naive method):", time.time() - start)

start = time.time()
compute('intersection')
print("Time (intersection method):", time.time() - start)
