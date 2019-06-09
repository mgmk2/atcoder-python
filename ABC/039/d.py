import itertools

h, w = map(int, input().split())

# 端の画素も処理できるように周囲を1マス分拡張することに注意
image = [['#'] + list(input()) + ['#'] for i in range(h)]
ans = [[image[i][j] if 0 < j < w + 1 else '.' for j in range(w + 2)] for i in range(h)]
image = [['#'] * (w + 2)] + image + [['#'] * (w + 2)]
ans = [['.'] * (w + 2)] + ans + [['.'] * (w + 2)]

# 答えの候補(ans)を作成
# imageの白の箇所では、収縮前は周囲8方向すべて白だったはず
for i, j in itertools.product(range(h), range(w)):
    if image[i + 1][j + 1] == '.':
        for k, l in itertools.product(range(3), range(3)):
            ans[i + k][j + l] = '.'

# 答えの候補を収縮(image2)
image2 = [[ans[i][j] for j in range(w + 2)] for i in range(h + 2)]
for i, j in itertools.product(range(h), range(w)):
    if ans[i + 1][j + 1] == '#':
        for k, l in itertools.product(range(3), range(3)):
            image2[i + k][j + l] = '#'

# image2とimageが一致すればpossible
for i, j in itertools.product(range(1, h + 1), range(1, w + 1)):
    if image[i][j] != image2[i][j]:
        print('impossible')
        break
else:
    print('possible')
    for si in ans[1:-1]:
        print(''.join(si[1:-1]))
