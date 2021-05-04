n = int(input())

ans = 1
a = 2
s = set()
while a * a <= n:
    k = a * a
    while k <= n:
        s.add(k)
        k *= a
    a += 1
print(n - len(s))