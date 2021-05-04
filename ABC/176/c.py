n = int(input())
a = list(map(int, input().split()))
pre = 0
ans = 0
for ai in a:
    if ai < pre:
        ans += pre - ai
    else:
        pre = ai
print(ans)
