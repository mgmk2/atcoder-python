n = int(input())
s = input()
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = ''
for i in range(len(s)):
    idx = n + a.find(s[i])
    ans += a[idx % 26]
print(ans)
