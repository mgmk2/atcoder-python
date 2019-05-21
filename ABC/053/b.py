s = input()
l = len(s)
for i, si in enumerate(s):
    if si == 'A':
        l -= i
        break
for i, si in enumerate(s[::-1]):
    if si == 'Z':
        l -= i
        break
print(l)
