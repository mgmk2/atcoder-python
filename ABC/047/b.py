w, h, n = map(int, input().split())
a = [0, w, 0, h]
for i in range(n):
    xi, yi, ai = map(int, input().split())
    if ai == 1:
        a[0] = max(xi, a[0])
    elif ai == 2:
        a[1] = min(xi, a[1])
    elif ai == 3:
        a[2] = max(yi, a[2])
    else:
        a[3] = min(yi, a[3])
print(max(0, a[1] - a[0]) * max(0, a[3] - a[2]))
