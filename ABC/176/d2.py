def dfs(xt, yt, S, V, w):
    B = set()
    while(len(S) > 0):
        xi, yi = S.pop()
        A = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                if i == 0 and j == 0:
                    continue
                xj, yj = xi + i, yi + j
                if xj < 0 or len(V) <= xj or yj < 0 or len(V[0]) <= yj:
                    continue
                if -1 <= i <= 1 and -1 <= j <= 1 and i * j == 0:
                    A.append((xj, yj))
                else:
                    B.add((xj, yj))

        for xj, yj in A:
            if xj == xt and yj == yt:
                return False, B, V, w
            if V[xj][yj] > 0:
                V[xj][yj] = -1
                S.append((xj, yj))

    B_new = []
    for x, y in B:
        if x == xt and y == yt:
            return False, B, V, w + 1
        if V[x][y] > 0:
            V[x][y] = -1
            B_new.append((x, y))
    return True, B_new, V, w

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch -= 1
cw -= 1
dh -= 1
dw -= 1

s = [list(map(lambda x: int(x == '.'), list(input()))) for _ in range(h)]

flag = True
B = [(ch, cw)]
w = -1
s[ch][cw] = -1
while flag:
    flag, B, s, w = dfs(dh, dw, B, s, w + 1)
    if flag and len(B) == 0:
        print(-1)
        break
else:
    print(w)
