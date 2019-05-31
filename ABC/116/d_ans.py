n, k = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(n)]
sushi.sort(key=lambda x: x[1])
t = {}
x = []
z = 0
for i in range(n - 1, n - k - 1, -1):
    ti, di = sushi[i]
    if ti in t.keys():
        x.append(di)
        t[ti] += 1
    else:
        t[ti] = 1
    z += di

p = len(t.keys())
ans = z + p ** 2
idx = 1
for i in range(n - k - 1, -1, -1):
    if idx == len(x) + 1:
        break
    ti, di = sushi[i]
    if ti not in t.keys():
        t[ti] = 1
        z += di - x[-idx]
        p += 1
        idx += 1
        ans = max(ans, z + p ** 2)

print(ans)
