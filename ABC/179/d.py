MOD = 998244353
n, k = map(int, input().split())
seg = [list(map(int, input().split())) for _ in range(k)]

s = [0 for _ in range(n + 1)]
s[1] = 1
for i in range(1, n):
    s[i + 1] = s[i]
    for l, r in seg:
        s[i + 1] += (s[max(0, i - l + 1)] - s[max(0, i - r)]) % MOD
        s[i + 1] %= MOD
print((s[n] - s[n - 1]) % MOD)
