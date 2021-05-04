h, w, k = map(int, input().split())
c = [list(map(int, list(input().replace('.', '0').replace('#', '1')))) for _ in range(h)]
cs = [[0] for _ in range(h)]
y = 0
for i, ci in enumerate(c):
    for j, cij in enumerate(ci):
        cs[i].append(cs[i][-1])
        cs[i][-1] += c[i][j]
    y += cs[i][-1]
ans = 0
for i in range(2 ** h):
    for j in range(2 ** w):
        x = 0
        for ii in range(h):
            if (i >> ii) & 1:
                x += cs[ii][-1]
            else:
                for jj in range(j):
                    if (j >> jj) & 1:
                        x += c[ii][jj]
        ans += (y - x == k)
print(ans)
