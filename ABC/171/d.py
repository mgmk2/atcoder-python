from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
q = int(input())
x = [list(map(int, input().split())) for _ in range(q)]

s = sum(a)
d = defaultdict(int)
for ai in a:
    d[ai] += 1

for xi in x:
    b, c = xi
    s += d[b] * (c - b)
    print(s)
    d[c] += d[b]
    d[b] = 0
