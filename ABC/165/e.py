n, m = map(int, input().split())
ans = []
l = n // 2
r = n // 2 + 1

for i in range(m):
    ans.append((l, r))
    l -= 1
    r += 1
    l %= n
    r %= n
for a in ans:
    print(*a)
