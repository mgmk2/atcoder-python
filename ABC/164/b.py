a, b, c, d = map(int, input().split())
x = (a + d - 1) // d
y = (b + c - 1) // b
if x >= y:
    print('Yes')
else:
    print('No')
