n, m, k = map(int, input().split())
MOD = 998244353
ans = 0
p = 1
px = 1
py = 1
for i in range(k + 1):
    x = m * pow(m - 1, n - 1 - i, MOD) % MOD
    ans += p * x % MOD
    ans %= MOD

    px *= pow(i + 1, MOD - 2, MOD)
    py *= n - i - 1
    px %= MOD
    py %= MOD
    p = px * py % MOD
print(ans)
