a, b, c = map(int, input().split())
if a + b + c in [2 * a, 2 * b, 2 * c]:
    print('Yes')
else:
    print('No')
