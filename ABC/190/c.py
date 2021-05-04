from collections import defaultdict

n, m = map(int, input().split())
cond = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
choices = [list(map(int, input().split())) for _ in range(k)]

ans = 0
for i in range(2 ** k):
    x = defaultdict(int)
    for j, (c, d) in enumerate(choices):
        x[d if i & (1 << j) else c] += 1
    
    ans_i = 0
    for a, b in cond:
        if x[a] > 0 and x[b] > 0:
            ans_i += 1
    ans = max(ans, ans_i)
print(ans)