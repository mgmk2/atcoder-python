s = input()
t = input()
ans = sum([si == ti for si, ti in zip(s, t)])
print(ans)
