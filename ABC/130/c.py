w, h, x, y = map(int, input().split())
s = w * h / 2
if 2 * x == w and 2 * y == h:
    t = 1
else:
    t = 0
print(s, t)
