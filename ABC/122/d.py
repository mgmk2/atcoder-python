#   A C G T
# A
# C
# G
# T

import numpy as np

N = int(input())
x = 10 ** 9 + 7

S = np.ones([4, 4, 4], dtype=np.int64)
S[0, 1, 2] = 0
S[0, 2, 1] = 0
S[2, 0, 1] = 0
for _ in range(3, N):
    St = np.zeros([4, 4, 4], dtype=np.int64)
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 2:
                St[j, :, 0] += S[i, j, :]
                St[j, :, 2] += S[i, j, :]
                St[j, :, 3] += S[i, j, :]
            else:
                for k in range(4):
                    St[j, k, 0] += S[i, j, k]
                    St[j, k, 3] += S[i, j, k]
                    if j == 0 and k == 1:
                        St[j, k, 1] += S[i, j, k]
                    elif (j == 0 and k == 2) or (j == 2 and k == 0):
                        St[j, k, 2] += S[i, j, k]
                    elif i == 0 and k == 2:
                        St[j, k, 2] += S[i, j, k]
                    else:
                        St[j, k, 1] += S[i, j, k]
                        St[j, k, 2] += S[i, j, k]
    S = St % x
print(np.sum(S) % x)
