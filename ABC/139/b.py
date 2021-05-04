def ceil(x, y):
    return (x + y - 1) // y

a, b = map(int, input().split())
print(ceil(b - 1, a - 1))
