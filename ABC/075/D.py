def in_rectangle(p, l, r, d, u):
    if (l <= p[0] <= r) and (d <= p[1] <= u):
        return True
    else:
        return False

n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
p.sort()
s = []
for g in range(n - 1):
    l = p[g][0]
    for h in range(g + 1, n):
        r = p[h][0]
        dd = min(p[g][1], p[h][1])
        uu = max(p[g][1], p[h][1])
        for i in range(n):
            if p[i][1] <= dd:
                d = p[i][1]
                for j in range(n):
                    if p[j][1] >= uu:
                        u = p[j][1]
                        m = 0
                        for t in range(g, h + 1):
                            if in_rectangle(p[t], l, r, d, u):
                                m += 1
                        if m >= k:
                            s.append((r - l) * (u - d))
print(min(s))
