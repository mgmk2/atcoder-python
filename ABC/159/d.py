from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
for ai in a:
    d[ai] += 1
s = 0
for v in d.values():
    s += v * (v - 1) // 2
c = {}
for k, v in d.items():
    c[k] = s - v * (v - 1) // 2 + max(0, (v - 1) * (v - 2) // 2)
for ai in a:
    print(c[ai])
