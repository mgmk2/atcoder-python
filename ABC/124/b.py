n = int(input())
h = list(map(int, input().split()))
hm = 0
ans = 0
for hi in h:
    if hm <= hi:
        ans += 1
        hm = hi
print(ans)
