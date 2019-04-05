n, h = map(int, input().split())
a = [None for _ in range(n)]
b = [None for _ in range(n)]
ans = 0
for i in range(n):
    a[i], b[i] = map(int, input().split())
a_s = sorted(a)[::-1]
b_s = sorted(b)[::-1]
for i in range(n):
    if b_s[i] >= a_s[0]:
        h -= b_s[i]
        ans += 1
        if h <= 0:
            break
    else:
        break
if h > 0:
    ans += (h + a_s[0] - 1) // a_s[0]
print(ans)
