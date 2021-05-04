import bisect

n = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(n - 2):
    a = L[i]
    for j in range(i + 1, n - 1):
        b = L[j]
        k = bisect.bisect_left(L, a + b)
        ans += k - j - 1
print(ans)
