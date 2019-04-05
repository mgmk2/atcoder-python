h, w = map(int, input().split())
s = [['#' for _ in range(w + 2)]]
s = s + [['#'] + list(input()) + ['#'] for _ in range(h)]
s = s + [['#' for _ in range(w + 2)]]
n_white = 0
for i in range(1, h + 1):
    n_white += s[i].count('.')
q = [[1, 1]]
a = []
d = 1
while(True):
    qq = []
    for i in range(len(q)):
        if q[i] in a:
            continue
        x = q[i][0]
        y = q[i][1]
        if s[x][y - 1] == '.' and [x, y - 1] not in qq:
            qq.append([x, y - 1])
        if s[x - 1][y] == '.' and [x - 1, y] not in qq:
            qq.append([x - 1, y])
        if s[x + 1][y] == '.' and [x + 1, y] not in qq:
            qq.append([x + 1, y])
        if s[x][y + 1] == '.' and [x, y + 1] not in qq:
            qq.append([x, y + 1])
    d += 1
    if [h, w] in qq:
        break
    elif qq == []:
        print(-1)
        exit()
    a = a + q
    q = qq
print(n_white - d)
