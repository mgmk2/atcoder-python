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

INF = 10 ** 15
n, m = map(int, input().split())
V = [[INF, 0] for _ in range(n + 1)]
E = []
for i in range(m):
    ai, bi, ci = map(int, input().split())
    E.append([ai, bi, -ci])
V, negative = bellman_ford(1, V, E)
if negative[n]:
    print('inf')
else:
    i = n
    ans = 0
    while(i != 1):
        d, i = V[i]
        ans += d
    print(-V[n][0])
