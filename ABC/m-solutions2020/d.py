n = int(input())
a = list(map(int, input().split()))
# dp[day]
dp = [0 for j in range(n)]
dp[0] = 1000
for i in range(n):
    # buy stocks at i-th day.
    ai = a[i]
    m = dp[i]
    s = m // ai

    # sell stocks at j-th day.
    for j in range(i + 1, n):
        dp[j] = max(dp[j], m + s * (a[j] - ai))

    for j in range(n - 1):
        dp[j + 1] = max(dp[j + 1], dp[j])
print(dp[-1])
