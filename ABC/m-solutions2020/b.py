a, b, c = map(int, input().split())
k = int(input())
x = 0
while a >= b:
    b *= 2
    x += 1
while b >= c:
    c *= 2
    x += 1
if x <= k:
    print('Yes')
else:
    print('No')
