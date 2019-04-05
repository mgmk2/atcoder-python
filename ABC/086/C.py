N = int(input())
tt = 0
xx = 0
yy = 0
z = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    t, x, y = z[i]
    dt = t - tt
    dx = abs(x - xx)
    dy = abs(y - yy)
    if dt < dx + dy or (dt - (dx + dy)) % 2:
        print('No')
        exit()
    tt = t
    xx = x
    yy = y
print('Yes')
