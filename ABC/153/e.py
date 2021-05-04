h, n = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
a, b = x[0]
dp = [-(-i // a) * b for i in range(h + 1)]
for j in range(1, n):
    a, b = x[j]
    for i in range(min(h + 1, a)):
        dp[i] = min(dp[i], b)
    for i in range(a, h + 1):
        dp[i] = min(dp[i], dp[i - a] + b)
print(dp[-1])
