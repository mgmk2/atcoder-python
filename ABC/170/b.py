x, y = map(int, input().split())
if 2 * x <= y <= 4 * x and y % 2 == 0:
    print('Yes')
else:
    print('No')
