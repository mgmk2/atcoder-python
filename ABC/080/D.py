n, c = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
x.sort()
rec = [x[0]]
for i in range(1, n):
    xx = x[i]
    flag = True
    for j in range(len(rec)):
        if rec[j][1] <= xx[0] - 0.5:
            rec[j] = xx
            flag = False
    if flag:
        rec.append(xx)
print(len(rec))
