import numpy as np

h, w, k = map(int, input().split())
x = [list(map(int, list(input()))) for _ in range(h)]
x = np.array(x, np.int)

ans = []
for i in range(2 ** (h - 1)):
    ib = bin(i)[2:]
    h_range = [0]
    for j, c in enumerate(ib):
        if c == '1':
            h_range.append(j + 1)
    h_range.append(h)
    ch = len(h_range) - 2
    xi = np.zeros([ch + 1, w], np.int)
    for j in range(ch + 1):
        xi[j, :] = np.sum(x[h_range[j]:h_range[j + 1], :], axis=0)
    y = np.zeros([ch + 1], np.int)
    cw = 0
    for j in range(w):
        if xi[:, j].max() > k:
            break
        elif np.amax(y + xi[:, j]) > k:
            y = xi[:, j]
            cw += 1
        else:
            y += xi[:, j]
    else:
        ans.append(ch + cw)
print(min(ans))
