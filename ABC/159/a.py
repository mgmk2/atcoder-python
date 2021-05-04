n, m = map(int, input().split())
print(max(0, n * (n - 1) // 2) + max(0, m * (m - 1) // 2))
