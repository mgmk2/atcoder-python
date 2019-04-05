a, b = map(int, input().split())
x = b - a + 1
n = len(bin(b)[2:])
#z = (x + x % (y // 2)) % 2
ans = ''

for i in range(n):
    y = 2 ** (i + 1)
    if a % y == 0:
        z = 0
        w = 0
    else:
        w = min(b - a + 1, y - a % y)
        z = min(w, y // 2)
    print(w)
    print(z)
    if y - a % y <= b - a + 1:
        v = max(0, b - a + 1 - w)
        z += v // y * (y // 2) + max(0, v % y - (y // 2))
    print(z)
    ans += str(z % 2)
    print()
print(int(ans[::-1], 2))
