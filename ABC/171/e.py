n = int(input())
a = list(map(int, input().split()))
s = 0
for ai in a:
    s = s ^ ai

ans = []
for ai in a:
    ans.append((s & ~ai) + (~s & ai))
print(*ans)
