n, w = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for j in range(w + 1)] for i in range(2)]

for i, (wi, vi) in enumerate(x):
    dp_pre = dp[1 - i % 2]
    dp_cur = dp[i % 2]
    for j in range(1, wi):
        dp_cur[j] = dp_pre[j]
    for j in range(wi, w + 1):
        dp_cur[j] = max(dp_pre[j], dp_pre[j - wi] + vi)
print(max(dp_cur))
