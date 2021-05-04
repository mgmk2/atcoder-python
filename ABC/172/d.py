from functools import reduce

n = int(input())
def f(x, y):
    k = n // y
    return x + k * (y + y * k) // 2

ans = reduce(f, range(n + 1))
print(ans)
