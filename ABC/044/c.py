n, a = map(int, input().split())
x = list(map(int, input().split()))
x_max = max(x)
x_sum = sum(x)
ans = 0
if x_max >= a:
    dp = [[[0 for k in range(x_sum + 1)] for j in range(n + 1)] for i in range(2)]
    dp[0][0][0] = 1
    for i in range(1, n + 1):
        idx = i % 2
        for j in range(n + 1):
            for k in range(x[i - 1]):
                dp[idx][j][k] = dp[1 - idx][j][k]
            if j > 0:
                for k in range(x[i - 1], x_sum + 1):
                    dp[idx][j][k] = dp[1 - idx][j][k] + dp[1 - idx][j - 1][k - x[i - 1]]

    for j in range(1, min(x_sum // a + 1, n + 1)):
        ans += dp[idx][j][j * a]
print(ans)
