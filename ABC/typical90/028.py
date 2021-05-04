n = int(input())

LX, LY, RX, RY = 1000, 1000, 0, 0

inputs = []
for i in range(n):
    lx, ly, rx, ry = map(int, input().split())
    LX = min(LX, lx)
    LY = min(LY, ly)
    RX = max(RX, rx)
    RY = max(RY, ry)
    inputs.append((lx, ly, rx, ry))

X = RX - LX + 1
Y = RY - LY + 1

z = [[0 for j in range(Y + 1)] for i in range(X + 1)]
a = [[0 for j in range(Y + 2)] for i in range(X + 2)]

for lx, ly, rx, ry in inputs:
    z[lx - LX][ly - LY] += 1
    z[rx - LX][ry - LY] += 1
    z[lx - LX][ry - LY] -= 1
    z[rx - LX][ly - LY] -= 1

ans = [0 for _ in range(n)]
for i in range(X):
    for j in range(Y):
        aij = a[i + 1][j] + a[i][j + 1] - a[i][j] + z[i][j]
        a[i + 1][j + 1] = aij
        if aij > 0:
            ans[aij - 1] += 1

print(*ans, sep='\n')
