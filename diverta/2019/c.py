n = int(input())
c = [0, 0, 0]
ans = 0
for i in range(n):
    si = input()
    ans += si.count('AB')
    if si[0] == 'B' and si[-1] == 'A':
        c[0] += 1
    elif si[0] == 'B':
        c[1] += 1
    elif si[-1] == 'A':
        c[2] += 1
ans += max(0, c[0] - 1)
if c[0] > 0 and c[1] > 0:
    ans += 1
    c[1] -= 1
if c[0] > 0 and c[2] > 0:
    ans += 1
    c[2] -= 1
ans += max(0, min(c[1:]))
print(ans)
