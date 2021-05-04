k, x = map(int, input().split())
lower = max(x - k + 1, -1000000)
upper = min(x + k - 1, 1000000)
print(*tuple(range(lower, upper + 1)))
