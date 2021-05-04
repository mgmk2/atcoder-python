import bisect

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = [0]
for i in range(n):
    sa.append(sa[-1] + a[i])
sb = [0]
for i in range(m):
    sb.append(sb[-1] + b[i])
ans = 0
for i, s in enumerate(sa):
    if s > k:
        break
    ans = max(ans, i + max(0, bisect.bisect_left(sb, k - s + 1) - 1))
print(ans)
