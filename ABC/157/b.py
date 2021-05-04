a = [list(map(int, input().split())) for _ in range(3)]
c = [[False for j in range(3)] for i in range(3)]
n = int(input())
ans = False

for k in range(n):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if a[i][j] == b:
                c[i][j] = True

for i in range(3):
    flag1 = 1
    flag2 = 1
    for j in range(3):
        flag1 *= c[i][j]
        flag2 *= c[j][i]
    if flag1 or flag2:
        ans = True
        break

if not ans:
    flag1 = 1
    flag2 = 1
    for i in range(3):
        flag1 *= c[i][i]
        flag2 *= c[i][2 - i]
    if flag1 or flag2:
        ans = True

if ans:
    print('Yes')
else:
    print('No')
