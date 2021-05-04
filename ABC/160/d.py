n, x, y = map(int, input().split())
x -= 1
y -= 1
d = [0 for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        if j <= x or i >= y:
            d[j - i] += 1
        else:
            k = min(j - i, abs(x - i) + abs(y - j) + 1)
            d[k] += 1
for ans in d[1:]:
    print(ans)
