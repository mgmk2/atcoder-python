n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[1] = abs(a[1] - a[0])
for i in range(2, n):
    x1 = dp[i - 1] + abs(a[i] - a[i - 1])
    x2 = dp[i - 2] + abs(a[i] - a[i - 2])
    dp[i] = min(x1, x2)
print(dp[-1])
