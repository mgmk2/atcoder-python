from collections import defaultdict

n, s = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
MOD = 998244353
for l in range(n):
    f = [0 for _ in range(n)]
    c = defaultdict(int)
    for r in range(l, n):
        f[r] = (f[r - 1] + c[r]) % MOD
        f[r] %= MOD
        c[r] += 1
print(ans)
