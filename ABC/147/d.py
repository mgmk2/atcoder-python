n = int(input())
a = list(map(int, input().split()))
L = len(format(max(a), 'b'))
x = [0 for i in range(L)]
ans = 0
MOD = 10 ** 9 + 7
for i in a:
    i_str = list(format(i, '0' + str(L) + 'b'))[::-1]
    for j, s in enumerate(i_str):
        if s == '1':
            x[j] += 1
b = 1
for i, xi in enumerate(x):
    ans += xi * (n - xi) * b % MOD
    ans %= MOD
    b *= 2
    b %= MOD
print(ans)
