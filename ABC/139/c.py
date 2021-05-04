n = int(input())
h = list(map(int, input().split()))
h_pre = h[0]
k = 0
ans = 0
for hi in h[1:]:
    if hi <= h_pre:
        k += 1
    else:
        ans = max(ans, k)
        k = 0
    h_pre = hi
print(max(ans, k))
