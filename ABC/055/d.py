n = int(input())
s = [1 if si == 'o' else 0 for si in list(input())]
t0 = [[1, 1], [1, 0], [0, 1], [0, 0]]
for ti in t0:
    flag = True
    for i in range(1, n - 1):
        if ti[i] * (1 - s[i]) or (1 - ti[i]) * s[i]:
            ti.append(1 - ti[i - 1])
        else:
            ti.append(ti[i - 1])
    for i in range(2):
        if ti[i - 1]:
            if (s[i - 1] and not ti[i - 2] == ti[i]) or (1 - s[i - 1] and ti[i - 2] == ti[i]):
                flag = False
        else:
            if (s[i - 1] and ti[i - 2] == ti[i]) or (1 - s[i - 1] and not ti[i - 2] == ti[i]):
                flag = False
    if flag:
        ans = ['S' if x else 'W' for x in ti]
        print(''.join(ans))
        exit()
print(-1)
