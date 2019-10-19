a, b = map(int, input().split())
x = a + b
if x % 2:
    print('IMPOSSIBLE')
else:
    print(x // 2)
