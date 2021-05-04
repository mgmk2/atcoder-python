n, L = map(int, input().split())
x = list(map(int, input().split()))
t = list(map(int, input().split()))
dp = [10 ** 9 for _ in range(L + 1)]
dp[0] = 0
k = 0
for i in range(L):
    if k < n and i == x[k]:
        p = t[2]
        k += 1
    else:
        p = 0
    ti = dp[i]
    dp[i + 1] = min(dp[i + 1], ti + t[0] + p)
    if i < L - 1:
        dp[i + 2] = min(dp[i + 2], ti + t[0] + t[1] + p)
    else:
        dp[i + 1] = min(dp[i + 1], ti + t[0] // 2 + t[1] // 2 + p)
    if i < L - 3:
        dp[i + 4] = min(dp[i + 4], ti + t[0] + t[1] * 3 + p)
    else:
        for j in range(i + 1, L + 1):
            dp[j] = min(dp[j], ti + t[0] // 2 + t[1] // 2 + t[1] * (j - (i + 1)) + p)
print(dp[-1])
