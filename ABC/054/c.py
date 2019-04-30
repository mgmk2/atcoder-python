def find_path(x, v, e):
    if len(v) == len(e):
        return 1
    ans = 0
    for xi in e[x - 1]:
        if xi in v:
            continue
        vi = v + [xi]
        ans += find_path(xi, vi, e)
    return ans

n, m = map(int, input().split())
e = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    e[a - 1].append(b)
    e[b - 1].append(a)
ans = find_path(1, [1], e)
print(ans)
