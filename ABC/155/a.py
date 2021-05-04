a, b, c = map(int, input().split())
if (a == b) + (b == c) + (c == a) == 1:
    print('Yes')
else:
    print('No')
