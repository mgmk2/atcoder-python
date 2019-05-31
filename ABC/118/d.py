n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
b = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [0 for _ in range(n + 1)]
INF = 10 ** 9
for i in range(1, n + 1):
    c = [dp[i - b[aj]] for aj in a if i >= b[aj]]
    if len(c) > 0:
        dp[i] = max(c) + 1
    else:
        dp[i] = -INF

x = n
i = 0
ans = ''
while(True):
    for aj in a:
        if x - b[aj] >= 0 and dp[x - b[aj]] == dp[n] - i - 1:
            i += 1
            x -= b[aj]
            ans += str(aj)
            break
    if i == dp[n]:
        break
print(ans)
