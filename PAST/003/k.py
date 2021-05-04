n, q = map(int, input().split())
t = [i for i in range(n + 1)]
c = [0 for _ in range(n + 1)]
for i in range(q):
    fi, ti, xi = map(int, input().split())
    t[ti], t[fi], c[xi] = t[fi], c[xi], t[ti]

ans = [0 for _ in range(n)]
for i in range(1, n + 1):
    x = t[i]
    if x == 0:
        continue
    while x > 0:
        ans[x - 1] = i
        x = c[x]
print(*ans, sep='\n')
