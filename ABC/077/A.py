c = [list(input()) for _ in range(2)]
for i in range(3):
    if c[0][i] != c[1][-i-1]:
        print('NO')
        exit()
print('YES')
