from collections import defaultdict

def dfs(i, V, E, x):
    S = [i]
    while(len(S) > 0):
        vi = S.pop()
        p = x[vi]
        for j in E[vi]:
            if V[j] == 0:
                V[j] = 1
                x[j] += p
                S.append(j)
    return V, x

n, q = map(int, input().split())
V = [0 for _ in range(n + 1)]
E = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

x = [0 for _ in range(n + 1)]
for i in range(q):
    pi, xi = map(int, input().split())
    x[pi] += xi

V[1] = 1
dfs(1, V, E, x)
print(*x[1:])
