n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
for i in range(n):
    for j in range(2):
        xi = min(a[i + j], b[i])
        a[i + j] -= xi
        b[i] -= xi
        x += xi
print(x)
