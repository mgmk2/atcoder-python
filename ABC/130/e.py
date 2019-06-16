n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
MOD = 10 ** 9 + 7
dp = [[[0, 0] for j in range(m + 1)] for i in range(n + 1)]
for i, si in enumerate(s):
    for j, tj in enumerate(t):
        if si == tj:
            dp[i + 1][j + 1][0] = (dp[i][j][1] + 1) % MOD
        dp[i + 1][j + 1][1] = (dp[i + 1][j][1] + dp[i][j + 1][1] - dp[i][j][1] + dp[i + 1][j + 1][0]) % MOD
print(dp)
