from collections import defaultdict

n, c = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(c)]
p = [defaultdict(int), defaultdict(int), defaultdict(int)]
for i in range(n):
    ci = list(map(int, input().split()))
    for j, cj in enumerate(ci):
        k = (i + j + 2) % 3
        p[k][cj] += 1
ans = []
for i in range(1, c + 1):
    x = 0
    for ci, ti in p[0].items():
        x += D[ci - 1][i - 1] * ti

    for j in range(1, c + 1):
        if j == i:
            continue
        y = 0
        for cj, tj in p[1].items():
            y += D[cj - 1][j - 1] * tj

        for k in range(1, c + 1):
            if k in [i, j]:
                continue
            z = 0
            for ck, tk in p[2].items():
                z += D[ck - 1][k - 1] * tk
            ans.append(x + y + z)

print(min(ans))
