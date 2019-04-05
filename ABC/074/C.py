a, b, c, d, e, f = map(int, input().split())
x = []
y = []
t = 100 * e / (100 + e)
for i in range(f // (100 * a) + 1):
    bb = f - 100 * a * i
    for j in range(bb // (100 * b) + 1):
        if 100 * (a * i + b * j) in x:
            continue
        else:
            x.append(100 * (a * i + b * j))
for i in range(f // c + 1):
    dd = f - c * i
    for j in range(dd // d + 1):
        if c * i + d * j in y:
            continue
        else:
            y.append(c * i + d * j)
y.sort()
rr = 0
ans = []
for i, xi in enumerate(x):
    for j, yi in enumerate(y):
        if xi + yi == 0:
            continue
        r = 100 * yi / (xi + yi)
        if r > t:
            break
        elif xi + yi <= f and rr <= r:
            ans = [xi + yi, yi]
            rr = r
print(ans[0], ans[1])
