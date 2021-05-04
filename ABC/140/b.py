n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_pre = -1
ans = 0
for ai in a:
    ans += b[ai - 1]
    if ai == a_pre + 1:
        ans += c[a_pre - 1]
    a_pre = ai
print(ans)
