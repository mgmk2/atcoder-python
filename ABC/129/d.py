import numpy as np

h, w = map(int, input().split())
x = [list(input()) for _ in range(h)]
L = np.zeros([h + 2, w + 2], dtype=int)
U = np.zeros([h + 2, w + 2], dtype=int)
R = np.zeros([h + 2, w + 2], dtype=int)
D = np.zeros([h + 2, w + 2], dtype=int)
for i in range(h):
    for j in range(w):
        if x[i][j] == '.':
            L[i + 1, j + 1] = L[i + 1, j] + 1
            U[i + 1, j + 1] = U[i, j + 1] + 1
        if x[h - i - 1][w - j - 1] == '.':
            R[h - i, w - j] = R[h - i, w - j + 1] + 1
            D[h - i, w - j] = D[h - i + 1, w - j] + 1
ans = (L + R + D + U).max() - 3
print(ans)
