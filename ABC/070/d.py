def dfs(i, V, E):
    S = [i]
    while(len(S) > 0):
        vi = S.pop()
        d = V[vi]
        for j, value in E[vi].items():
            if V[j] > value + d:
                V[j] = value + d
                S.append(j)
    return V

INF = 10 ** 14
n = int(input())
V = [INF for _ in range(n + 1)]
E = [{} for _ in range(n + 1)]
for i in range(n - 1):
    ai, bi, ci = map(int, input().split())
    E[ai][bi] = ci
    E[bi][ai] = ci

q, k = map(int, input().split())
z = [list(map(int, input().split())) for _ in range(q)]
V[k] = 0

V = dfs(k, V, E)
for i in range(q):
    x, y = z[i]
    print(V[x] + V[y])
