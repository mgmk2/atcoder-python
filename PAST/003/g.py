from collections import deque

n, x, y = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(n)]

p = (0, 0)
Q = deque()
Q.append((0, p))
S = set()
while len(Q) > 0:
    k, (qx, qy) = Q.popleft()
    L = [(qx + i, qy + 1) for i in range(-1, 2)] \
        + [(qx + 1, qy), (qx - 1, qy)] \
        + [(qx, qy - 1)]
    if (x, y) in L:
        print(k + 1)
        break
    for l in L:
        if -201 <= l[0] <= 201 and -201 <= l[1] <= 201:
            if l in A or l in S:
                continue
            Q.append((k + 1, l))
            S.add(l)
else:
    print(-1)
