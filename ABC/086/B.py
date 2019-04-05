a, b = list(input().split())
c = int(a + b)
if c ** 0.5 % 1 == 0:
    print('Yes')
else:
    print('No')
