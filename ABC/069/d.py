h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
X = [[0 for j in range(w)] for i in range(h)]

xi = -1
hi = 0
for i, ai in enumerate(a):
    for j in range(xi + 1, min(xi + ai + 1, w)):
        X[hi][j] = i + 1
    if j == w - 1:
        hi += 1
        j = -1
        for j in range(max(0, xi + ai + 1 - w)):
            X[hi][j] = i + 1
    xi = j

for i in range(h):
    if i % 2 == 0:
        print(*X[i])
    else:
        print(*X[i][::-1])
