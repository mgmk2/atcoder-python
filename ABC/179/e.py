n, x, m = map(int, input().split())

v = list(range(m))
p = [-1 for _ in range(m)]

a = x
p[a - 1] = 0
s = [x]
l, r = n, n
for i in range(n):
    a = a ** 2 % m
    if p[a - 1] >= 0:
        l, r = p[a - 1], i + 1
        break
    else:
        s.append(a)
        p[a - 1] = i + 1
ans = sum(s[:l])
if l != r:
    b = (n - 1 - i) // (r - l) + 1
    c = (n - 1 - i) % (r - l)
    ans += b * sum(s[l:r]) + sum(s[l:l + c])
print(ans)
