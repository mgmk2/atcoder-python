n = int(input())
f = [list(map(int, input().split())) for _ in range(n)]
p = [list(map(int, input().split())) for _ in range(n)]
total = -10**10
for i in range(1, 1024):
    x = list(map(int, list(format(i, '010b'))))
    tmp = 0
    for j in range(n):
        a = 0
        for k in range(10):
            a += x[k] * f[j][k]
        tmp += p[j][a]
    total = max(tmp, total)
print(total)
