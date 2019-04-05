def dfs(x, y, k, z):
    for l in z:
        if x[k][l] == 1 and l not in y:
            y.append(l)
            y = dfs(x, y, l, z)
    return y

n, m = map(int, input().split())
a = [None for _ in range(n)]
for i in range(n):
    a[i] = [0 for _ in range(n)]

bridge = []
for i in range(m):
    s, t = map(int, input().split())
    a[s - 1][t - 1] = 1
    a[t - 1][s - 1] = 1
    bridge.append([s - 1, t - 1])

d = [list(range(n))]
for p in range(m):
    a[bridge[p][0]][bridge[p][1]] = 0
    a[bridge[p][1]][bridge[p][0]] = 0
    b = []
    c = []
    for j in range(len(d)):
        for i in range(n):
            if i not in b:
                tmp = dfs(a, [i], i, d[j])
                b += tmp
                c.append(tmp)
    ans = 0
    if len(c) > 1:
        ans = 0
        for i in range(len(c)):
            ans += len(c[i]) * (n - len(c[i]))
        ans = ans // 2
    else:
        ans = 0
    print(ans)
