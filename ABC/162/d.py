n = int(input())
s = input()

a = {}
a['R'] = [0 for _ in range(n + 1)]
a['G'] = [0 for _ in range(n + 1)]
a['B'] = [0 for _ in range(n + 1)]

for i, si in enumerate(s):
    a['R'][i + 1] += a['R'][i]
    a['G'][i + 1] += a['G'][i]
    a['B'][i + 1] += a['B'][i]
    a[si][i + 1] += 1

ans = 0
for i, si in enumerate(s):
    if si == 'R':
        keys = ['G', 'B']
    elif si == 'G':
        keys = ['B', 'R']
    else:
        keys = ['R', 'G']
    x = a[keys[0]][-1] - a[keys[0]][i + 1]
    y = a[keys[1]][-1] - a[keys[1]][i + 1]
    ans += x * y
    for j in range(1, (n - i + 1) // 2):
        sj = s[i + j]
        sk = s[i + 2 * j]
        if sj != sk and sj in keys and sk in keys:
            ans -= 1
print(ans)
