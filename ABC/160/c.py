k, n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
pre = a[-1] - k
x = 0
for ai in a:
    x = max(x, ai - pre)
    pre = ai
print(k - x)
