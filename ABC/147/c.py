n = int(input())
a = [[] for i in range(n)]
for i in range(n):
    ai = int(input())
    for j in range(ai):
        x = list(map(int, input().split()))
        a[i].append(x)
ans = 0
for i in range(2 ** n):
    i_str = format(i, '0' + str(n) + 'b')
    flag = False
    z = [-1 for _ in range(n)]
    h = []
    for j in range(n):
        if i_str[j] == '1':
            h.append(j)
    for j in h:
        for x, y in a[j]:
            if z[x - 1] >= 0 and z[x - 1] != y:
                flag = True
                break
            elif z[x - 1] < 0:
                z[x - 1] = y
        if flag:
            break
    else:
        for zj, sj in zip(z, i_str):
            if zj >= 0 and zj != int(sj):
                flag = True
                break
    if not flag:
        ans = max(ans, sum(map(int, i_str)))
print(ans)
