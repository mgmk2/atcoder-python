n, a, b = map(int, input().split())
k = n // (a + b) * a + min(a, n % (a + b))
print(k)
