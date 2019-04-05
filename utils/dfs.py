def dfs(i, V, E):
    V[i] = 1
    Vi = [j for j in range(len(V)) if E[i][j] == 1 and V[j] == 0]
    for j in Vi[::-1]:
        V = dfs(j, V, E)
    return V
