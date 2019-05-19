r, g, b, n = map(int, input().split())
c = sorted([r, g, b])[::-1]
ans = 0
for i in range(n // c[0] + 1):
    x = n - i * c[0]
    for j in range(x // c[1] + 1):
        y = x - j * c[1]
        if y < 0:
            break
        elif y % c[2] == 0:
            ans += 1
print(ans)
