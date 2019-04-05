n, *x = list(map(int, input().split()))
L = [int(input()) for _ in range(n)]
L.sort()
i = 0
while(True):
    flag = True
    for j in range(len(L)):
        if x[i] == L[j]:
            del x[i]
            flag = False
            break
    if flag:
        i += 1
    if i >= len(x):
        break
if len(x) == 0:
    ans = [0]
else:
    c = [0]
    L = [L]
    ans = []
    while(True):
        ci = []
        Li = []
        for i in range(len(c)):
            if ans == [] or c[i] < min(ans):
                for j in range(len(L[i])):
                    for k in range(len(L[i])):
                        if j == k or L[i][j] + L[i][k] > 2 * x[0]:
                            continue
                        else:
                            ci.append(c[i] + 10)
                            Li.append(L[i][:])
                            Li[-1].append(L[i][j] + L[i][k])
                            del Li[-1][j], Li[-1][k]
                    if L[i][j] < x[0]:
                        ci.append(c[i] + 1)
                        Li.append(L[i][:])
                        Li[-1][j] += 1
                    if L[i][j] > x[-1]:
                        ci.append(c[i] + 1)
                        Li.append(L[i][:])
                        Li[-1][j] -= 1
        c = ci
        L = Li
        if ans == [] or min(c) < min(ans):
            for i in range(len(c)):
                for j in range(len(x)):
                    flag = False
                    for k in range(len(L[i])):
                        if x[j] == L[i][k]:
                            flag = True
                            break
                    if flag:
                        continue
                    else:
                        break
                if flag and (ans == [] or c[i] < min(ans)):
                    ans.append(c[i])

        else:
            break
        if ans != []:
            print(min(c))
            print(min(ans))
print(min(ans))
