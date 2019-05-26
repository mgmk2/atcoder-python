n, m = map(int, input().split())
l, r = 1, n
for i in range(m):
    li, ri = map(int, input().split())
    l = max(li, l)
    r = min(ri, r)
print(max(0, r - l + 1))
