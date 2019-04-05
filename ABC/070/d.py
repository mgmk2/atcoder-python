def warshall_floyd(V, E):
    INF = 10 ** 10
    d = [[INF for j in range(V)] for i in range(V)]
    for i, j, c in E:
        d[i - 1][j - 1] = c
        d[j - 1][i - 1] = c
    for k in range(V):
        for i in range(V - 1):
            for j in range(i, V):
                dk = d[i][k] + d[k][j]
                if d[i][j] > dk:
                    d[i][j] = dk
                    d[j][i] = dk
    return d

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
d = warshall_floyd(N, E)

Q, K = map(int, input().split())
for i in range(Q):
    x, y = map(int, input().split())
    print(d[x - 1][K - 1] + d[K - 1][y - 1])
