n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    xi, yi = p[i]
    for j in range(i + 1, n):
        xj, yj = p[j]
        dx = xi - xj
        dy = yi - yj
        if abs(dx) >= abs(dy):
            ans += 1
print(ans)
