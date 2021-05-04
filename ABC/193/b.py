n = int(input())

ans = None
for i in range(n):
    a, p, x = map(int, input().split())

    if x - a > 0:
        ans = p if ans is None else min(ans, p)
if ans is None:
    print(-1)
else:
    print(ans)