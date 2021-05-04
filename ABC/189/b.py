n, x = map(int, input().split())
y = [list(map(int, input().split())) for _ in range(n)]
a = 0
for i, (v, p) in enumerate(y):
    a += v * p
    if a > x * 100:
        print(i + 1)
        break
else:
    print(-1)