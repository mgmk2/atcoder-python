from collections import defaultdict

L = 0
R = 1

n = int(input())
d = defaultdict(lambda: [10 ** 9, -10 ** 9])
s = set()
d[0] = [0, 0]
for i in range(n):
    x, c = map(int, input().split())
    d[c][L] = min(d[c][L], x)
    d[c][R] = max(d[c][R], x)
    s.add(c)
colors = [0] + sorted(list(s))

dp = [[0, 0] for _ in range(len(colors))]
for i in range(len(colors) - 1):
    ci = colors[i]
    ci1 = colors[i + 1]
    dp[i + 1][L] = abs(d[ci1][L] - d[ci1][R]) + min(
        dp[i][L] + abs(d[ci][L] - d[ci1][R]),
        dp[i][R] + abs(d[ci][R] - d[ci1][R])
        )
    dp[i + 1][R] = abs(d[ci1][L] - d[ci1][R]) + min(
        dp[i][L] + abs(d[ci][L] - d[ci1][L]),
        dp[i][R] + abs(d[ci][R] - d[ci1][L])
        )

print(min(dp[-1][L] + abs(d[ci1][L]), dp[-1][R] + abs(d[ci1][R])))