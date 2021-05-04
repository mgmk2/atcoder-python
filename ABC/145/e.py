n, t = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
x.sort()
a_max = x[-1][0]

dp_pre = [0 for j in range(t + a_max)]
dp = [0 for j in range(t + a_max)]
for ai, bi in x:
    for j in range(ai):
        dp[j] = dp_pre[j]
    for j in range(ai, t + ai):
        dp[j] = max(dp_pre[j], dp_pre[j - ai] + bi)
    for j in range(t + ai, t + a_max):
        dp[j] = dp_pre[j]
    dp_pre, dp = dp, dp_pre
print(max(dp_pre))
