def bfs(i, V, E, depth=None):
    V[i] = 1
    Q = [i]
    d = 1
    while(True):
        Qi = []
        for q in Q:
            Vi = [j for j in range(len(V)) if E[q][j] == 1 and V[j] == 0]
            for v in Vi:
                V[v] = d
                Qi.append(v)
        if len(Qi) == 0 or (depth is not None and d == depth):
            break
        else:
            Q = Qi
            d += 1
    return V
