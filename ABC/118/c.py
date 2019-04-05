def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))
x = a[0]
for i in range(1, n):
    x = gcd(x, a[i])
print(x)
