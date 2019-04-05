s = list(input())
t = list(input())
Rs = {}
Rt = {}
for i in range(len(s)):
    if s[i] in Rs:
        if Rs[s[i]] != t[i]:
            print('No')
            exit()
    else:
        Rs[s[i]] = t[i]
    if t[i] in Rt:
        if Rt[t[i]] != s[i]:
            print('No')
            exit()
    else:
        Rt[t[i]] = s[i]
print('Yes')
