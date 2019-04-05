n = int(input())
k = int(input())
x = 1
for i in range(1, n + 1):
    x *= 2
    if x > k:
        break
x += k * (n - i)
print(x)
