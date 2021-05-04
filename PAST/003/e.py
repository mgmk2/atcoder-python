n, m, q = map(int, input().split())
E = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
V = [None] + list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(q)]
for si in s:
    if si[0] == 1:
        x = si[1]
        ci = V[x]
        print(ci)
        for vi in E[x]:
            V[vi] = ci
    else:
        _, x, y = si
        print(V[x])
        V[x] = y
