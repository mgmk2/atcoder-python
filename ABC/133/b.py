n, d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n - 1):
    xi = x[i]
    for j in range(i + 1, n):
        xj = x[j]
        y = 0
        for k in range(d):
            y += (xi[k] - xj[k]) ** 2
        y_sqrt = int(y ** 0.5)
        if y_sqrt ** 2 == y:
            ans += 1
print(ans)
