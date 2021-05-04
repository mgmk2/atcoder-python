n = int(input())
p = list(map(float, input().split()))

dp = [0 for j in range(n + 1)]
dp[0] = 1
for i in range(n):
    pi = p[i]
    for j in range(i, -1, -1):
        dp[j + 1] = dp[j + 1] * pi + dp[j] * (1 - pi)
    dp[0] *= pi
print(sum(dp[:n // 2 + 1]))
