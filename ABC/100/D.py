import numpy as np
N, M = map(int, input().split())
W = [list(map(int, input().split())) for _ in range(N)]
W = np.array(W, dtype=np.int64)
t_max = 0
for i in range(8):
    a = np.array([(-1)**i, (-1)**(i // 2), (-1)**(i // 4)], dtype=np.int64)
    s = np.sum(a * W, axis=1)
    idx = np.argsort(s)[::-1]
    t = np.sum(np.abs(np.sum(W[idx[:M], :], axis=0)))
    if t > t_max:
        t_max = t
print(t_max)
