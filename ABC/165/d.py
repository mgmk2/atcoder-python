a, b, n = map(int, input().split())
ans = 0
# floor(a * x / b)
# = floor(a * floor(x / b) + a * (x / b - floor(x / b)))
# = a * floor(x / b) + floor(a * (x / b - floor(x / b))))
print(int(a * min(b - 1, n) / b))
