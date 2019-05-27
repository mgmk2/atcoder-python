from collections import defaultdict

h, w, n = map(int, input().split())
d = defaultdict(int)
for i in range(n):
    a, b = map(int, input().split())
    for k in range(max(1, a - 2), min(h - 2, a) + 1):
        for l in range(max(1, b - 2), min(w - 2, b) + 1):
            x = (k, l)
            d[x] += 1
ans = [0] * 10
for v in d.values():
    ans[v] += 1
ans[0] = (h - 2) * (w - 2) - sum(ans[1:])
for i in range(10):
    print(ans[i])
