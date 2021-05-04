from collections import defaultdict
import heapq

INF = 1e15

def dijkstra(i, N, E):
    T = [INF for i in range(N)]
    T[i] = 0
    Q = [(t, v) for v, t in enumerate(T)]
    heapq.heapify(Q)

    while len(Q) > 0:
        tu, u = heapq.heappop(Q)
        for v, t, k in E[u]:
            tv = tu + t
            if tu % k > 0:
                tv += k - tu % k
            if T[v] is None or T[v] > tv:
                T[v] = tv
                heapq.heappush(Q, (tv, v))
    return T

n, m, x, y = map(int, input().split())

E = defaultdict(list)

for i in range(m):
    a, b, t, k = map(int, input().split())
    E[a - 1].append((b - 1, t, k))
    E[b - 1].append((a - 1, t, k))

T = dijkstra(x - 1, n, E)
if T[y - 1] >= INF:
    print(-1)
else:
    print(T[y - 1])