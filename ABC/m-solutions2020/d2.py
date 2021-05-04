n = int(input())
a = list(map(int, input().split()))
a_cur = a[0]

m = 1000
s = 0

for i in range(1, n):
    a_next = a[i]
    if a_cur < a_next:
        # buy
        s += m // a_cur
        m -= s * a_cur
    else:
        # sell
        m += s * a_cur
        s = 0
    a_cur = a_next
m += s * a_cur
print(m)
