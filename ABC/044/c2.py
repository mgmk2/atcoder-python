n, a = map(int, input().split())
x = list(map(int, input().split()))
x_max = max(x)
x_sum = sum(x)
ans = 0
if x_max >= a:
    dp = [[0 for j in range(2 * x_sum + 1)] for i in range(2)]
    dp[0][x_sum] = 1
    for i in range(1, n + 1):
        idx = i % 2
        y = x[i - 1] - a
        for j in range(2 * x_sum + 1):
            if 0 <= j - y <= 2 * x_sum:
                dp[idx][j] = dp[1 - idx][j] + dp[1 - idx][j - y]
            else:
                dp[idx][j] = dp[1 - idx][j]
    ans = dp[n % 2][x_sum] - 1
print(ans)
