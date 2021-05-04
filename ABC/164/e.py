from collections import defaultdict
import heapq

def ceil(x, y):
    return (x + y - 1) // y

n, m, s = map(int, input().split())

E = defaultdict(dict)
for i in range(m):
    u, v, a, b = map(int, input().split())
    E[u - 1][v - 1] = (b, a)
    E[v - 1][u - 1] = (b, a)

penalty = [list(map(int, input().split())) for _ in range(n)]

INF = 2 * 10 ** 9
D = [INF for v in range(n)]
D[0] = 0
Q = [(d, v, 0, 0) for v, d in enumerate(D)]
heapq.heapify(Q)
prev = [None for v in range(n)]

while len(Q) > 0:
    du, u, au, tu = heapq.heappop(Q)
    p0, p1 = penalty[tu]
    ru = p1 / p0
    for v, (duv, auv) in E[u].items():
        pv0, pv1 = penalty[v]
        rv = pv1 / pv0
        av = au + auv
        dv = du + duv
        if ru > rv:
            if av > s:
                dv += ceil(av, pv0) * pv1
            tv = v
        else:
            if av > s:
                dv += ceil(av, p0) * p1
            tv = tu

        if D[v] > dv:
            D[v] = dv
            prev[v] = u
            heapq.heappush(Q, (dv, v, av, tv))

for i in range(1, n):
    print(D[i])
