input = open('06.in').read().strip()

def solve(scope):
    i = 0
    ans = None
    while i < len(input)-scope+1:
        s = set(input[i:i+scope])
        if len(s) == scope:
            ans = i+scope
            break
        i += 1
    return ans

print("Part 1:", solve(4))
print("Part 2:", solve(14))