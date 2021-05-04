n, d, h = map(int, input().split())

a, b = 0, 0
k = None

for i in range(n):
    di, hi = map(int, input().split())
    a = d - di
    b = h - hi
    k = b / a if k is None else min(k, b / a)

y = k * (-d) + h
print(max(0, y))
