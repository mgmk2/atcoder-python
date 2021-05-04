s = input()
q = int(input())
p = 1
pre = ''
post = ''
for i in range(q):
    x = input().split()
    if len(x) == 1:
        p *= -1
    else:
        f = int(x[1])
        c = x[2]
        if (p > 0 and f == 1) or (p < 0 and f == 2):
            pre += c
        else:
            post += c
if p < 0:
    print(post[::-1] + s[::-1] + pre)
else:
    print(pre[::-1] + s + post)
