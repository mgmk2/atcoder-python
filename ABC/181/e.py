import bisect

n, m = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

h.sort()

d_odd = [0]
for hi in h[1::2]:
    d_odd.append(hi + d_odd[-1])
d_even = [0]
for hi in h[::2]:
    d_even.append(hi + d_even[-1])

ans = None
for wi in w:
    k = bisect.bisect_left(h, wi)
    if k % 2:
        s = d_odd[k // 2] - d_even[k // 2 + 1] + wi + (d_even[-1] - d_even[k // 2 + 1]) - (d_odd[-1] - d_odd[k // 2])
    else:
        s = d_odd[k // 2] - d_even[k // 2] - wi + (d_even[-1] - d_even[k // 2]) - (d_odd[-1] - d_odd[k // 2])
    ans = s if ans is None else min(ans, s)
print(ans)
