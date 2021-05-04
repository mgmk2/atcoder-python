a, b = map(int, input().split())
# a <= x * 1.08 < a + 1
# b <= x * 1.1 < b + 1
x_min = min(int(a / 0.08), int(b / 0.1))
x_max = max(int((a + 1) / 0.08), int((b + 1) / 0.1))
for x in range(x_min, x_max + 1):
    if int(x * 0.08) == a and int(x * 0.1) == b:
        print(x)
        break
else:
    print(-1)
