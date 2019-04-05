n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ss = list(set(s))
tmp = 0
ans = 0
for i in range(len(ss)):
    tmp = s.count(ss[i]) - t.count(ss[i])
    ans = max(ans, tmp)
print(ans)
