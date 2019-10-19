s = input()
n = len(s)
s0 = s[0]
numr = 1
numl = 0
ans = [0 for _ in range(n)]
for i in range(1, n):
    s1 = s[i]
    if s1 == 'R':
        numr += 1
    elif s1 == 'L':
        numl += 1

    if s0 == 'R' and s1 == 'L':
        ir = i - 1
        il = i
        ans[ir] += (numr + 1) // 2
        ans[il] += numr // 2
        numr = 0
    if (s0 == 'L' and s1 == 'R') or i == n - 1:
        ans[ir] += numl // 2
        ans[il] += (numl + 1) // 2
        numl = 0
    s0 = s1
print(*ans)
