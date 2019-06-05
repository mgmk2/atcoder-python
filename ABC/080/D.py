n, c = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
x.sort(key=lambda x: [x[-1], x[0]])
ans = [0 for _ in range(2 * 10 ** 5 + 2)]
cc = -1
for i in range(n):
    si, ti, ci = x[i]
    if ci != cc:
        tt = [0 for _ in range(2 * 10 ** 5 + 2)]
    for j in range(2 * si - 1, 2 * ti):
        if tt[j] == 0:
            tt[j] = 1
            ans[j] += 1
    cc = ci
print(max(ans))
