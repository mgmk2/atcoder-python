n, m = map(int, input().split())
E = [0 for _ in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    E[y - 1] += 1 << (x - 1)
dp = [0 for i in range(1 << n)]
dp[0] = 1
for i in range(1 << n):
    for y, x in enumerate(E):
        yy = 1 << y
        if (i & yy) and not (i & x):
            dp[i] += dp[i - yy]
print(dp[-1])
