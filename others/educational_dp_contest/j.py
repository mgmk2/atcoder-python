def rec(i, j, k, n, dp):
    if dp[i][j][k] >= 0:
        return dp[i][j][k]
    if i + j + k == 0:
        return 0

    x = n
    if i > 0:
        x += rec(i - 1, j, k, n, dp) * i
    if j > 0:
        x += rec(i + 1, j - 1, k, n, dp) * j
    if k > 0:
        x += rec(i, j + 1, k - 1, n, dp) * k
    x /= i + j + k
    dp[i][j][k] = x
    return x

n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(3)]

for i, ai in enumerate(a):
    b[ai - 1] += 1

dp = [[[-1 for k in range(n + 1)] for j in range(n + 1)] for i in range(n + 1)]

print(rec(b[0], b[1], b[2], n, dp))
