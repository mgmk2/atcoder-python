n = int(input())
s = [int(input()) for _ in range(n)]
s.sort()
ans = sum(s)
x = [ans]
if ans % 10 == 0:
    i = 0
    while(True):
        for j in range(len(x)):
            x.append(x[j] - s[i])
        x = list(set(x))
        x.sort(reverse=True)
        flag = False
        for xi in x:
            if xi % 10 > 0:
                print(xi)
                flag = True
                break
        if flag:
            break
        elif i == n - 1:
            print(0)
            break
        else:
            i += 1
else:
    print(ans)
