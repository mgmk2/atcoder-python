import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 5 + 100)

def rec(v, dp, E):
    if dp[v] != -1:
        return dp[v]
    x = 0
    for w in E[v]:
        x = max(x, rec(w, dp, E) + 1)
    dp[v] = x
    return x

n, m = map(int, input().split())
E = defaultdict(list)
for i in range(m):
    x, y = map(int, input().split())
    E[x - 1].append(y - 1)

dp = [-1 for _ in range(n)]
ans = 0
for i in range(n):
    ans = max(ans, rec(i, dp, E))
print(ans)
