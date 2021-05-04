def warshall_floyd(V, E):
    INF = 10 ** 9
    d = [[0 for _ in range(V + 1)]] + [[0] + [INF for j in range(V)] for i in range(V)]
    for i in range(V + 1):
        d[i][i] = 0
    for i, j in E:
        d[i][j] = 1
        d[j][i] = 1
    for k in range(1, V + 1):
        for i in range(1, V):
            for j in range(i, V + 1):
                dk = d[i][k] + d[k][j]
                if d[i][j] > dk:
                    d[i][j] = dk
                    d[j][i] = dk
    return d


h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
n = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            n += 1
            s[i][j] = n
        else:
            s[i][j] = 0


E = []
for i in range(h):
    for j in range(w):
        p = s[i][j]
        if p > 0:
            if j < w - 1:
                p1 = s[i][j + 1]
                if p1 > 0:
                    E.append([p, p1])
            if i < h - 1:
                p2 = s[i + 1][j]
                if p2 > 0:
                    E.append([p, p2])

ans = 0
INF = 10 ** 9
D = warshall_floyd(n, E)
ans = max(list(map(max, D)))
print(ans)
