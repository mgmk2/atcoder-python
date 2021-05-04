n, w = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

v = sum([vi for _, vi in x])
dp = [[2 * 10 ** 9 for j in range(v + 1)] for i in range(2)]
dp[0][0] = 0
dp[1][0] = 0

for i, (wi, vi) in enumerate(x):
    dp_pre = dp[1 - i % 2]
    dp_cur = dp[i % 2]
    for j in range(1, vi):
        dp_cur[j] = dp_pre[j]
    for j in range(vi, v + 1):
        dp_cur[j] = min(dp_pre[j], dp_pre[j - vi] + wi)
ans = 0
for vi, wi in enumerate(dp_cur):
    if wi <= w:
        ans = max(ans, vi)
print(ans)
