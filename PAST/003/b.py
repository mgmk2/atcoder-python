n, m, q = map(int, input().split())
x = [[] for _ in range(n)]
p = [n for _ in range(m)]
for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        ni = s[1]
        ans = 0
        for k in x[ni - 1]:
            ans += p[k]
        print(ans)
    else:
        _, ni, mi = s
        x[ni - 1].append(mi - 1)
        p[mi - 1] = max(0, p[mi - 1] - 1)
