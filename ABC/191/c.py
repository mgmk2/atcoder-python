h, w = map(int, input().split())
S = []
for i in range(h):
    S.append(list(input()))

edge = []
for i in range(h):
    pre = '.'
    left = None
    right = None
    for j in range(1, w):
        if pre == '.' and S[i][j] == '#':
            left = j
        elif pre == '#' and S[i][j] == '.':
            right = j - 1
        pre = S[i][j]
    if left is None and right is None:
        edge.append(None)
    else:
        edge.append((left, right))

ans = 2
pre = None
for i in range(h):
    if edge[i] is None:
        continue
    elif pre is None:
        ans += 2
    else:
        for j in range(2):
            if pre[j] != edge[i][j]:
                ans += 2
    pre = edge[i]
print(ans)