n, l = map(int, input().split())
x = 1000
a = 0
for i in range(1, n + 1):
    xi = l + i - 1
    if abs(x) > abs(xi):
        x = xi
    a += xi
print(a - x)
