n, m = map(int, input().split())
a = list(map(int, input().split()))
z = [ai for ai in a]

ans = None
roads = [list(map(int, input().split())) for _ in range(m)]
roads.sort()
for x, y in roads:
    x -= 1
    y -= 1
    ans = a[y] - z[x] if ans is None else max(ans, a[y] - z[x])
    z[y] = min(z[x], z[y])
print(ans)