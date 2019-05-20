import sys

sys.setrecursionlimit(10 ** 5 + 1)

def dfs(i, V, E):
    for k in E[i].keys():
        if V[k] >= 0:
            continue
        if E[i][k] % 2:
            V[k] = 1 - V[i]
        else:
            V[k] = V[i]
        V = dfs(k, V, E)
    return V

n = int(input())
E = {}
for i in range(n - 1):
    ui, vi, wi = map(int, input().split())
    if ui in E.keys():
        E[ui][vi] = wi
    else:
        E[ui] = {vi: wi}
    if vi in E.keys():
        E[vi][ui] = wi
    else:
        E[vi] = {ui: wi}
V = [-1 for _ in range(n + 1)]
V[1] = 0
V = dfs(1, V, E)
for vi in V[1:]:
    print(vi)
