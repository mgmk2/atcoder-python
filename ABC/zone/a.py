s = input()
k = 0
ans = 0
while k < len(s):
    if s[k:k + 4] == 'ZONe':
        ans += 1
        k += 4
    else:
        k += 1
print(ans)
