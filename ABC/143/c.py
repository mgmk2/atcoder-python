n = int(input())
s = input()
si_pre = ''
ans = 0
for si in s:
    if si_pre != si:
        ans += 1
    si_pre = si
print(ans)
