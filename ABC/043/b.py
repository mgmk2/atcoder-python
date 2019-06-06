s = input()
ans = []
for si in s:
    if si == 'B':
        if len(ans) > 0:
            ans.pop()
    else:
        ans.append(si)
print(''.join(ans))
