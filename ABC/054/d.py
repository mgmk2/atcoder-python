n, ma, mb = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
a_limit = [0]
b_limit = [0]
for i in range(n):
    a_limit.append(a_limit[-1] + x[i][0])
    b_limit.append(b_limit[-1] + x[i][1])

INF = 10 ** 9
DP = [None for _ in range(n + 1)]
for i in range(n + 1):
    DP[i] = [[INF for k in range(b_limit[-1] + 1)] for j in range(a_limit[-1] + 1)]

DP[0][0][0] = 0
for i in range(n):
    for j in range(a_limit[i] + 1):
        for k in range(b_limit[i] + 1):
            DP[i + 1][j][k] = min(DP[i + 1][j][k], DP[i][j][k])
            DP[i + 1][j + x[i][0]][k + x[i][1]] = min(DP[i + 1][j + x[i][0]][k + x[i][1]], DP[i][j][k] + x[i][2])

ans = INF
for j in range(1, a_limit[-1] + 1):
    for k in range(1, b_limit[-1] + 1):
        if k * ma == j * mb:
            ans = min(ans, DP[-1][j][k])
if ans == INF:
    print(-1)
else:
    print(ans)
