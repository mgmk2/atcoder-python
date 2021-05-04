s = input()
t = input()

ans = 0
for si, ti in zip(s, t):
    if si != ti:
        ans += 1
print(ans)
