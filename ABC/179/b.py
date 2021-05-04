n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
x = 0
for d1, d2 in d:
    if d1 == d2:
        x += 1
    else:
        x = 0
    if x == 3:
        print('Yes')
        break
else:
    print('No')
