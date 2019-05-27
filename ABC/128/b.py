n = int(input())
x = []
for i in range(n):
    s, p = input().split()
    p = -int(p)
    x.append([s, p, i + 1])
x.sort()
for i in range(n):
    print(x[i][2])
