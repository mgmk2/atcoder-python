n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    for j in range(-1, 2):
        if a[i] + j in d.keys():
            d[a[i] + j] += 1
        else:
            d[a[i] + j] = 1
print(max(d.values()))
