MOD = 10 ** 9 + 7

n, k = map(int, input().split())
x = [0 for _ in range(k + 1)]

ans = 0
for i in range(k, 0, -1):
    x[i] = pow(k // i, n, MOD)
    t = 0
    for j in range(2 * i, k + 1, i):
        x[i] -= x[j]
        x[i] %= MOD
    ans += i * x[i] % MOD
    ans %= MOD
print(ans)
