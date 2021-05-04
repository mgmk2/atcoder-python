from collections import defaultdict

INF = 10 ** 10

n, m = map(int, input().split())
a = list(map(int, input().split()))
z = [INF for i in range(n)]
E = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    E[x - 1].append(y - 1)
for i in range(n):
    for j in E[i]:
        z[j] = min(z[i], z[j], a[i])
ans = None
for i in range(n):
    d = a[i] - z[i]
    ans = d if ans is None else max(ans, d)
print(ans)