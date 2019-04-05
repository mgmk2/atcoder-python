n, k = map(int, input().split())
x = []
for i in range(n):
    x.append(list(map(int, input().split())))
x = sorted(x, key=lambda x: x[1])[::-1]
y = {}
z = [0]
for i in range(k):
    z[-1] += x[i][1]
    if x[i][0] in y.keys():
        y[x[i][0]] += 1
    else:
        y[x[i][0]] = 1
z[-1] += len(y.keys()) ** 2

j = 0
while(True):
    z.append(z[-1])
    flag0 = False
    for i in range(k - 1 - j, -1, -1):
        if y[x[i][0]] > 1:
            y[x[i][0]] -= 1
            z[-1] -= x[i][1]
            flag0 = True
            break
    flag1 = False
    for i in range(k + j, n):
        if x[i][0] not in y.keys():
            y[x[i][0]] = 1
            z[-1] += x[i][1]
            flag1 = True
            break
    if flag0 and flag1:
        z[-1] += 2 * len(y.keys()) - 1
    else:
        del z[-1]
        break
    if k + j + 1 == n or len(y.keys()) == k or z[-1] == z[-2]:
        break
    else:
        j += 1
print(max(z))
