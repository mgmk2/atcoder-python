k, s = map(int, input().split())
ans = 0
for x in range(min(s + 1, k + 1)):
    for y in range(min(s - x + 1, k + 1)):
        if s - x - y <= k:
            ans += 1
print(ans)
