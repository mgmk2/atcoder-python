n = int(input())
a = list(map(int, input().split()))
l, r = [i for i in range(n + 1) if a.count(a[i]) > 1]
x = 10 ** 9 + 7
total = n + 1
d = 1
print(n)
for k in range(1, n + 1):
    total = total * (n + 1 - k) // (k + 1)
    d = d * (l + n - r - k + 1) // k
    print((total - d) % x)
