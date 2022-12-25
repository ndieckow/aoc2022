import itertools

inp = open('25.in').read().split('\n')

nums = {
    '2' : 2,
    '1' : 1,
    '0' : 0,
    '-' : -1,
    '=' : -2
}

nums_inv = {
    4 : '-',
    3 : '=',
    2 : '2',
    1 : '1',
    0 : '0',
}

def snafu_to_dec(n):
    ans = 0
    dig = 1
    for c in n[::-1]:
        ans += nums[c]*dig
        dig *= 5
    return ans

def dec_to_snafu(n):
    ans = []
    while n > 0:
        div,rem = n // 5, n % 5
        ans.append(nums_inv[rem])
        n = div+1 if rem > 2 else div
    return ''.join(ans[::-1])

ans = 0
for line in inp:
    ans += snafu_to_dec(line)

print('Part 1:', dec_to_snafu(ans))
print('Part 2: Just collect all the other stars, bro')