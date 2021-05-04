h, w, x, y = map(int, input().split())
x -= 1
y -= 1
s = [input() for _ in range(h)]

ans = 1

for i in range(x):
    if s[x - i - 1][y] == '#':
        ans += i
        break
else:
    ans += x

for i in range(x + 1, h):
    if s[i][y] == '#':
        ans += i - x - 1
        break
else:
    ans += h - x - 1

for j in range(y):
    if s[x][y - j - 1] == '#':
        ans += j
        break
else:
    ans += y

for j in range(y + 1, w):
    if s[x][j] == '#':
        ans += j - y - 1
        break
else:
    ans += w - y - 1

print(ans)