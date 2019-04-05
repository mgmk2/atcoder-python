c = [list(map(int, input().split())) for _ in range(3)]
d = [c[0][0] - c[0][1], c[0][1] - c[0][2]]
for i in range(1, 3):
    if c[i][0] - c[i][1] != d[0] or c[i][1] - c[i][2] != d[1]:
        print('No')
        exit()
d = [c[0][0] - c[1][0], c[1][0] - c[2][0]]
for i in range(1, 3):
    if c[0][i] - c[1][i] != d[0] or c[1][i] - c[2][i] != d[1]:
        print('No')
        exit()
print('Yes')
