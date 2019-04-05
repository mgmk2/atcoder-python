N = int(input())
a = list(map(int, input().split()))
x = 0
y = 0

for ai in a:
    if ai % 4 == 0:
        x += 1
    elif ai % 2 == 1:
        y += 1
if x >= y or (x == y - 1 and x + y == N):
    print('Yes')
else:
    print('No')
