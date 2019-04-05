a, b = map(int, input().split())
x = (a % 3) * (b % 3)
if x == 0 or x == 2:
    print('Possible')
else:
    print('Impossible')
