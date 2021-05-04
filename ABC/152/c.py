n = int(input())
p = list(map(int, input().split()))
m = 10 ** 6
ans = 0
for pi in p:
    m = min(pi, m)
    if pi <= m:
        ans += 1
print(ans)
