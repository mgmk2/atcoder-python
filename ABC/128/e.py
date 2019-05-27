n, q = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
p.sort(key=lambda x: x[2])
d = [int(input()) for _ in range(q)]
k = 0
kk = 0
for i, di in enumerate(d):
    ans = -1
    for j in range(k, n):
        s, t, x = p[j]
        tj = x + di
        if s <= tj < t:
            ans = x
            k = kk
            break
        kk += 1
    print(ans)
