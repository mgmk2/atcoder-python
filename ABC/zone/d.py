from collections import deque
s = input()

t = deque()
k = 1
for si in s:
    if si == 'R':
        k *= -1
    elif len(t) == 0:
        t.append(si)
    elif k > 0:
        if t[-1] != si:
            t.append(si)
        else:
            t.pop()
    elif k < 0:
        if t[0] != si:
            t.appendleft(si)
        else:
            t.popleft()
ans = ''.join(t)
if k < 0:
    ans = ans[::-1]
print(ans)
