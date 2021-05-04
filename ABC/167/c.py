n, m, x = map(int, input().split())
c = [None for _ in range(n)]
a = [None for i in range(n)]
ans = None
for i in range(n):
    c[i], *ai = map(int, input().split())
    a[i] = list(ai)
for p in range(2 ** n):
    y = [0 for _ in range(m)]
    s = format(p, '0{:}b'.format(n))
    cp = 0
    for i, (si, ci) in enumerate(zip(s, c)):
        if si == '1':
            cp += ci
            for j in range(m):
                y[j] += a[i][j]
    for yj in y:
        if yj < x:
            break
    else:
        ans = cp if ans is None else min(ans, cp)
if ans is None:
    print(-1)
else:
    print(ans)
