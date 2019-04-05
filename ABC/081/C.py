from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = Counter(a)
mc = c.most_common()[::-1]
if k >= len(mc):
    print(0)
else:
    ans = 0
    for i in range(len(mc) - k):
        ans += mc[i][1]
    print(ans)
