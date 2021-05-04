from collections import defaultdict
import heapq

def dijkstra(i, V, E, INF=1e9):
    D = [INF for v in V]
    D[i] = 0
    Q = [(0, i)]
    heapq.heapify(Q)

    while len(Q) > 0:
        du, u = heapq.heappop(Q)
        for v, duv in E[u].items():
            dv = du + duv
            if D[v] > dv:
                D[v] = dv
                heapq.heappush(Q, (dv, v))
    return D

INF = 1e9

n, m = map(int, input().split())
E_self = [None for _ in range(n)]
V = list(range(n))
E_forward = defaultdict(dict)
E_backward = defaultdict(dict)
for i in range(m):
    a, b, c = map(int, input().split())
    if a == b:
        E_self[a - 1] = c if E_self[a - 1] is None else min(E_self[a - 1], c)
    else:
        E_forward[a - 1][b - 1] = min(c, E_forward[a - 1].get(b - 1, c))
        E_backward[b - 1][a - 1] = min(c, E_forward[b - 1].get(a - 1, c))

for i in range(n):
    D_forward = dijkstra(i, V, E_forward)
    D_backward = dijkstra(i, V, E_backward)
    ans = INF if E_self[i] is None else E_self[i]
    for j in range(n):
        if i == j:
            continue
        ans = min(ans, D_forward[j] + D_backward[j])
    print(ans if ans < INF else -1)