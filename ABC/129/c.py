n, m = map(int, input().split())
if m > 0:
    a = {int(input()): None for i in range(m)}
else:
    a = {}
dp = [0] * (n + 1)
dp[0] = 1
MOD = 10 ** 9 + 7
if m == 0 or 1 not in a:
    dp[1] = 1
for i in range(2, n + 1):
    if i - 1 not in a:
        dp[i] += dp[i - 1]
    if i - 2 not in a:
        dp[i] += dp[i - 2]
    dp[i] %= MOD
print(dp[-1])
