def ceil_div(x, y):
    return (x + y - 1) // y

n = int(input())
ans = 1
tt = 1
aa = 1
for i in range(n):
    t, a = map(int, input().split())
    x = t + a
    p = max(ceil_div(ans, x), ceil_div(tt, t), ceil_div(aa, a))
    ans = x * p
    aa = a * p
    tt = t * p
print(ans)
