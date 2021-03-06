def warshall_floyd(V, E):
    INF = 10 ** 9
    d = [[[INF, 0] for j in range(V + 1)] for i in range(V + 1)]
    for i, j, c in E:
        d[i][j] = [c, 0]
        d[j][i] = [c, 0]
    for k in range(1, V + 1):
        for i in range(1, V):
            for j in range(i, V + 1):
                dk = d[i][k][0] + d[k][j][0]
                if d[i][j][0] > dk:
                    d[i][j] = [dk, k]
                    d[j][i] = [dk, k]
    return d

def find_path(i, j, d, E):
    k = d[i][j][1]
    if k == 0:
        E[i][j] += 1
        E[j][i] += 1
        return E
    E = find_path(i, k, d, E)
    E = find_path(k, j, d, E)
    return E
