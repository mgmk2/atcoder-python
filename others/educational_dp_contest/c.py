n = int(input())
h = [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(2)]
for i, (a, b, c) in enumerate(h):
    dp[i % 2][0] = a + max(dp[1 - i % 2][1], dp[1 - i % 2][2])
    dp[i % 2][1] = b + max(dp[1 - i % 2][0], dp[1 - i % 2][2])
    dp[i % 2][2] = c + max(dp[1 - i % 2][0], dp[1 - i % 2][1])
print(max(dp[i % 2]))
