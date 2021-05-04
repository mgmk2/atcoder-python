h, w = map(int, input().split())
a = [None for _ in range(h)]
for i in range(h):
    a[i] = [s == '.' for s in input()]

MOD = 10 ** 9 + 7
dp = [[0 for j in range(w + 1)] for i in range(h + 1)]
dp[1][1] = 1
for i in range(h):
    for j in range(w):
        if a[i][j]:
            dp[i + 1][j + 1] += (dp[i][j + 1] + dp[i + 1][j]) % MOD
            dp[i + 1][j + 1] %= MOD
print(dp[-1][-1])
