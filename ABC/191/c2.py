h, w = map(int, input().split())
S = []
for i in range(h):
    S.append(list(input()))

ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        x = 0
        for ii in range(2):
            for jj in range(2):
                if S[i + ii][j + jj] == '#':
                    x += 1
        if x in [1, 3]:
            ans += 1
print(ans)