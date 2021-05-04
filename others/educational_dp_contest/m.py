MOD = 10 ** 9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0 for _ in range(k + 1)]
dp[0] = 1
b = [1 for _ in range(k + 2)]
b[0] = 0

for ai in a:
    for i in range(k, -1, -1):
        dp[i] += (b[i] - b[i - min(ai, i)]) % MOD
        dp[i] %= MOD
    for i in range(1, k + 2):
        b[i] = (b[i - 1] + dp[i - 1]) % MOD
        b[i] %= MOD
print(dp[-1])
