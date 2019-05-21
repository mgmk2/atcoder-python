import copy

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

n, m = map(int, input().split())
E = [[None for j in range(n + 1)] for i in range(n + 1)]
E_list = []
for i in range(m):
    a, b, c = map(int, input().split())
    E_list.append([a, b, c])
    E[a][b] = 0
    E[b][a] = 0
d = warshall_floyd(n, E_list)
ans = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        E = find_path(i, j, d, E)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if E[i][j] == 0:
            ans += 1
print(ans)
