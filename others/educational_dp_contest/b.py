n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [0 for _ in range(n)]
for i in range(1, n):
    hi = h[i]
    x = 2 * 10 ** 9
    for j in range(1, min(k, i) + 1):
        x = min(x, dp[i - j] + abs(hi - h[i - j]))
    dp[i] = x
print(dp[-1])
