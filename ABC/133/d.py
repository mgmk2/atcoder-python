n = int(input())
a = list(map(int, input().split()))
x = [sum(a) - 2 * sum(a[1::2])]
for i in range(n - 1):
    x.append(2 * a[i] - x[i])
print(*x)
