import itertools

n = int(input())
p = [list(map(int, input().split())) for _ in range(n)]

for p1, p2, p3 in itertools.combinations(p, 3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # ax + by + c = 0
    a = y2 - y1
    b = x1 - x2

    if a * x3 + b * y3 == a * x1 + b * y1:
        print('Yes')
        break
else:
    print('No')
