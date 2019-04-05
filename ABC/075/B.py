h, w = map(int, input().split())
s = [['.'] * (w + 2)]
s += [['.'] + list(input()) + ['.'] for _ in range(h)]
s += [['.'] * (w + 2)]
t = s
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] == '.':
            n = 0
            for k in range(3):
                n += s[i - 1 + k][j - 1:j + 2].count('#')
            t[i][j] = str(n)
for i in range(1, h + 1):
    tt =''
    for j in range(1, w + 1):
        tt += t[i][j]
    print(tt)
