from collections import defaultdict, deque

def bfs(start, end, V, E):
    V[start] = 0
    Q = deque()
    Q.append(start)
    while(len(Q) > 0 and V[end] < 0):
        q = Q.popleft()
        d = V[q] + 1
        for v in E[q]:
            if V[v] > 0:
                continue
            V[v] = d
            Q.append(v)
    return V

n, m = map(int, input().split())
E = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    E[u].append(n + v)
    E[n + u].append(2 * n + v)
    E[2 * n + u].append(v)
s, t = map(int, input().split())
V = [-1] * (3 * n + 1)
V = bfs(s, t, V, E)
if V[t] < 0:
    print(-1)
else:
    print(V[t] // 3)
