h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
p_min = []
for i in range(10):
    p = c[i]
    for j in range(10):
        pp = p
        for k in range(10):
            for l in range(10):
                pp[k] = min(pp[k], p[l] + c[l][k])
        p = pp
    p_min.append(p[1])
a = [list(map(int, input().split())) for _ in range(h)]
ans = 0
for i in range(10):
    count = 0
    for j in range(h):
        count += a[j].count(i)
    ans += count * p_min[i]
print(ans)
