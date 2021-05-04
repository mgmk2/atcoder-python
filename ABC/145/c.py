def dist(x1, x2):
    d2 = (x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2
    return d2 ** 0.5

n = int(input())
x = [list(map(int, input().split())) for _ in range(n)]
d = 0
for i in range(n - 1):
    xi = x[i]
    for j in range(i + 1, n):
        d += dist(xi, x[j])
print(2 * d / n)
