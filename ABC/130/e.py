n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
MOD = 10 ** 9 + 7
dp = [[0 for j in range(m + 1)] for i in range(2)]
for i, si in enumerate(s):
    for j, tj in enumerate(t):
        idx = (i + 1) % 2
        dp[idx][j + 1] = (dp[idx][j] + dp[1 - idx][j + 1] - dp[1 - idx][j]) % MOD
        if si == tj:
            dp[idx][j + 1] += dp[1 - idx][j] + 1
        dp[idx][j + 1] %= MOD
print((dp[n % 2][-1] + 1) % MOD)
