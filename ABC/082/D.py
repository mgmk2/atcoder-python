s = input()
x, y = map(int, input().split())
a = 0
t = [[0], [0]]
n = 0
for i in range(len(s)):
    if s[i] == 'F':
        t[n][-1] += 1
    else:
        n = 1 - n
        t[n].append(0)
flag = [False, False]
for k in range(2):
    tt = t[k]
    z = [x, y]
    if k == 0:
        p = [tt[0]]
    else:
        p = [tt[0], -tt[0]]
    for i in range(1, len(tt)):
        pp = []
        for j in range(len(p)):
            pp.append(p[j] + tt[i])
            pp.append(p[j] - tt[i])
        p = pp
    if z[k] in p:
        flag[k] = True
if flag[0] and flag[1]:
    print('Yes')
else:
    print('No')
