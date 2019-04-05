n = int(input())
key = input()
x = {}
x[key] = None
s = list(key)[-1]
flag = True
for i in range(n - 1):
    xx = input()
    if xx not in x and s == list(xx)[0]:
        x[xx] = None
        s = list(xx)[-1]
    else:
        flag = False
if flag:
    print('Yes')
else:
    print('No')
