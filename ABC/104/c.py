D, G = map(int, input().split())
p = [None for _ in range(D)]
c = [None for _ in range(D)]
s = [None for _ in range(D)]
for i in range(D):
    p[i], c[i] = map(int, input().split())
    s[i] = 100 * (i + 1) * p[i] + c[i]

INF = 10 ** 9
ans = []
for i in range(2 ** D):
    ii = bin(i)[2:]
    ii = '0' * (D - len(ii)) + ii
    y = 0
    x = 0
    for j in range(D):
        if ii[j] == '1':
            y += s[j]
            x += p[j]
    yy = G - y
    if yy > 0:
        xx = sum(p)
        flag = False
        for j in range(D):
            xt = x
            if ii[j] == '0':
                ss = 100 * (j + 1)
                if (yy + ss - 1) // ss < p[j]:
                    xt += (yy + ss - 1) // ss
                    if xt < xx:
                        xx = xt
                        flag = True
        if flag:
            x = xx
        else:
            x = INF
    ans.append(x)
print(min(ans))
