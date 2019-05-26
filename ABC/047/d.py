n, t = map(int, input().split())
a = list(map(int, input().split()))
a_min = a[0]
d = 0
x = 0
for i in range(1, n):
    di = a[i] - a_min
    if d < di:
        d = di
        x = 1
    elif d == di:
        x += 1
    a_min = min(a_min, a[i])
print(x)
