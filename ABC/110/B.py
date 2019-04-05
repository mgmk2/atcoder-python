n, m, x, y = map(int, input().split())
xx = list(map(int, input().split()))
yy = list(map(int, input().split()))
xx.append(x)
yy.append(y)
if max(xx) >= min(yy):
    print('War')
else:
    print('No War')
