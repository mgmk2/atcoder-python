import heapq
from collections import defaultdict

def dijkstra(i, V, E, INF=1e9):
    D = {v: INF for v in V}
    D[i] = 0
    Q = [(d, v) for v, d in D.items()]
    heapq.heapify(Q)
    prev = {v: None for v in V}

    while len(Q) > 0:
        du, u = heapq.heappop(Q)
        for v, duv in E[u].items():
            dv = du + duv
            if D[v] > dv:
                D[v] = dv
                prev[v] = u
                heapq.heappush(Q, (dv, v))
    return D

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch -= 1
cw -= 1
dh -= 1
dw -= 1

s = [list(input()) for _ in range(h)]
V = []
E = defaultdict(dict)
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        V.append((i, j))

        for k in range(-2, 3):
            for l in range(-2, 3):
                if k == 0 and l == 0:
                    continue
                x = i + k
                y = j + l
                if x < 0 or x >= h or y < 0 or y >= w or s[x][y] == '#':
                    continue
                if (k, l) in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    E[(i, j)][(x, y)] = 0
                    E[(x, y)][(i, j)] = 0
                else:
                    E[(i, j)][(x, y)] = 1
                    E[(x, y)][(i, j)] = 1

INF = 1e9
D = dijkstra((ch, cw), V, E, INF=INF)

if D[(dh, dw)] == INF:
    print(-1)
else:
    print(D[(dh, dw)])
