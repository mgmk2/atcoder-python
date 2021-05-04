from collections import deque, defaultdict

def bfs(i, V, E):
    S = deque()
    S.append(i)
    V[i] = 1
    while(len(S) > 0):
        vi = S.popleft()
        for j in E[vi]:
            if V[j] == 0:
                V[j] = vi
                S.append(j)
    return V

n, m = map(int, input().split())
V = [0 for _ in range(n + 1)]
E = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
V = bfs(1, V, E)
print('Yes')
print(*V[2:], sep='\n')
