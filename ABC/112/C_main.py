N = int(input())
x = [None for _ in range(N)]
y = [None for _ in range(N)]
h = [None for _ in range(N)]
for i in range(N):
    x[i], y[i], h[i] = map(int, input().split())
    if h[i] > 0:
        a = [x[i], y[i], h[i]]
for cx in range(0, 101):
    for cy in range(0, 101):
        hh = a[2] + abs(a[0] - cx) + abs(a[1] - cy)
        flag = True
        for i in range(N):
            h_i = max(hh - abs(x[i] - cx) - abs(y[i] - cy), 0)
            if h_i != h[i]:
                flag = False
        if flag:
            print(cx, cy, hh)
            exit()
