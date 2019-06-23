import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
ans = 0;
for bj in b:
    ai = bisect.bisect_left(a, bj);
    ck = n - bisect.bisect_right(c, bj);
    ans += ai * ck;
print(ans)
