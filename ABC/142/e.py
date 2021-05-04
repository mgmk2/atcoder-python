n, m = map(int, input().split())

x = [None for _ in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    c = map(int, input().split())
    t = sum(map(lambda x: 2 ** (x - 1), c))
    x[i] = (a, t)

INF = 10 ** 9
dp = [INF for _ in range(2 ** n)]
dp[0] = 0

for ai, ti in x:
    for j in range(2 ** n):
        dp[ti | j] = min(dp[ti | j], dp[j] + ai)

if dp[-1] >= INF:
    ans = -1
else:
    ans = dp[-1]
print(ans)
