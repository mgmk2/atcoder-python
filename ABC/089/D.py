h, w, d = map(int, input().split())
x = []
z = [None for i in range(h * w)]
for i in range(h):
    x.append(list(map(int, input().split())))
    for j in range(w):
        z[x[i][j] - 1] = [i + 1, j + 1]

s = [None for _ in range(d)]
for i in range(min(d, h * w - d + 1)):
    a = z[max(0, i - 1)]
    b = z[d + i - 1]
    s[i] = [abs(a[0] - b[0]) + abs(a[1] - b[1])]
    j = 1
    while(True):
        if d * (j + 1) + i <= h * w:
            a = z[d * j + i - 1]
            b = z[d * (j + 1) + i - 1]
            s[i].append(s[i][-1] + abs(a[0] - b[0]) + abs(a[1] - b[1]))
            j += 1
        else:
            break

Q = int(input())
ans = [None for _ in range(Q)]
for i in range(Q):
    L, R = map(int, input().split())
    if L == R:
        ans[i] = 0
    elif L // d - 1 < 0:
        ans[i] = s[R % d][R // d - 1]
    else:
        ans[i] = s[R % d][R // d - 1] - s[L % d][L // d - 1]
for i in range(Q):
    print(ans[i])
