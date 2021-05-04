from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

dp = defaultdict(int)
dm = defaultdict(int)
for i, ai in enumerate(a):
    if i + 1 + ai <= n:
        dp[i + ai + 1] += 1
    if 0 < i + 1 - ai <= n:
        dm[i + 1 - ai] += 1
ans = 0
keys = set(dp.keys()) & set(dm.keys())
for k in keys:
    ans += dp[k] * dm[k]
print(ans)
