def func(x):
    k = (x + 1) // 2
    if x % 2:
        y = k % 2
    else:
        y = (k % 2) ^ x
    return y

a, b = map(int, input().split())
print(func(b) ^ func(a - 1))
