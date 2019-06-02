from collections import defaultdict

s = input()
x, y = map(int, input().split())
a = 0
t = [[0], []]
n = 0
for i in range(len(s)):
    if s[i] == 'F':
        t[n][-1] += 1
    else:
        n = 1 - n
        t[n].append(0)
flag = [False, False]
z = [x, y]
for k in range(2):
    tt = t[k]
    zk = z[k]
    if len(tt) == 0:
        if zk == 0:
            flag = True
            continue
        else:
            print(1, k)
            flag = False
            break
    p = sum(tt)
    dp = defaultdict(bool)
    i = 1
    if k == 0:
        dp[tt[0]] = True
    else:
        dp[tt[0]] = True
        dp[-tt[0]] = True
    if len(tt) > 1:
        for tj in tt[1:]:
            dp2 = defaultdict(bool)
            for xj in dp.keys():
                dp2[xj + tj] = True
                dp2[xj - tj] = True
            dp = dp2
    flag = dp[zk]
    if not flag:
        break
if flag:
    print('Yes')
else:
    print('No')
