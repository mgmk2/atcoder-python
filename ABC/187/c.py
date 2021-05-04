n = int(input())
s = [input() for _ in range(n)]

s0 = set()
s1 = set()
for si in s:
    if si[0] == '!':
        s1.add(si[1:])
    else:
        s0.add(si)
ans = s0 & s1
if len(ans):
    print(ans.pop())
else:
    print('satisfiable')
