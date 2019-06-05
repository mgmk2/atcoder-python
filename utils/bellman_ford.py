def bellman_ford(x, V, E):
    V[x][0] = 0
    negative = [False for _ in range(len(V))]
    for i in range(len(V) - 2):
        for a, b, c in E:
            if V[b][0] > V[a][0] + c:
                V[b][0] = V[a][0] + c
                V[b][1] = a

    for a, b, c in E:
        if V[b][0] > V[a][0] + c:
            negative[b] = True
        elif negative[a]:
            negative[b] = True

    return V, negative
