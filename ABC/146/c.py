a, b, x = map(int, input().split())
n = []
for d in range(1, 10):
    y = x - b * d
    if y <= 0:
        break
    n.append(min(10 ** d - 1, y // a))
else:
    y = x - b * 10
    if y >= a * 10 ** 9:
        n.append(10 ** 9)
if len(n) == 0:
    print(0)
else:
    print(max(n))
