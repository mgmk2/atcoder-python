x, y, z, kk = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

p = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            if (i + 1) * (j + 1) * (k + 1) <= kk:
                p.append(a[i] + b[j] + c[k])
            else:
                break
p.sort(reverse=True)
for i in range(kk):
    print(p[i])
