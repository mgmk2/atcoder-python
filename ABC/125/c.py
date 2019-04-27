def divisor(x):
    y = list()
    for i in range(1, int(x ** 0.5 + 1)):
        if x % i == 0:
            y.append(i)
            y.append(x // i)
    return y

n = int(input())
a = list(map(int, input().split()))
a.sort()
d0 = divisor(a[0])
d1 = divisor(a[1])
d = dict.fromkeys(d0 + d1)
ans = 1
for di in sorted(list(d.keys()))[::-1]:
    flag = False
    ans_flag = True
    for ai in a:
        if ai % di != 0:
            if flag:
                ans_flag = False
                break
            else:
                flag = True
    if ans_flag:
        ans = di
        break
print(ans)
