n, m = map(int, input().split())
x = [list(map(int, input().split())) + [i] for i in range(m)]
x.sort()
tmp = 0
k = 0
z = [None for _ in range(m)]
for i in range(m):
    if tmp == x[i][0]:
        k += 1
    else:
        k = 1
        tmp = x[i][0]
    z[x[i][2]] = '{0:06d}{1:06d}'.format(x[i][0], k)
for i in range(m):
    print(z[i])
