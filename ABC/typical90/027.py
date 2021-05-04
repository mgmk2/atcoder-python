n = int(input())
x = set()
ans = []
for i in range(1, n + 1):
    s = input()
    if s not in x:
        x.add(s)
        ans.append(i)
print(*ans, sep='\n')
