INF = 10 ** 9
n, m, l = map(int, input().split())
d = [[INF for j in range(n + 1)] for i in range(n + 1)]
d2 = [[INF for j in range(n + 1)] for i in range(n + 1)]
for _ in range(m):
    i, j, c = map(int, input().split())
    d[i][j] = c
    d[j][i] = c
    if c <= l:
        d2[i][j] = 1
        d2[j][i] = 1

q = int(input())
Q = [list(map(int, input().split())) for _ in range(q)]

for k in range(1, n + 1):
    for i in range(1, n):
        for j in range(i, n + 1):
            dk = d[i][k] + d[k][j]
            if d[i][j] > dk:
                d[i][j] = dk
                d[j][i] = dk
                if dk <= l:
                    d2[i][j] = 1
                    d2[j][i] = 1

for k in range(1, n + 1):
    for i in range(1, n):
        for j in range(i, n + 1):
            dk = d2[i][k] + d2[k][j]
            if d2[i][j] > dk:
                d2[i][j] = dk
                d2[j][i] = dk

for i in range(q):
    s, t = Q[i]
    di = d2[s][t]
    if di >= INF:
        print(-1)
    else:
        print(di - 1)
