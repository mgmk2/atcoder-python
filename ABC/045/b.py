s = {}
l = {}
for si in ['a', 'b', 'c']:
    s[si] = list(input())[::-1]
    l[si] = len(s[si]) - 1
x = 'a'
while(True):
    if l[x] == -1:
        break
    xx = s[x][l[x]]
    l[x] -= 1
    x = xx
print(x.upper())
