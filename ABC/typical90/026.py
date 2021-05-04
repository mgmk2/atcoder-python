from collections import defaultdict

n = int(input())
E = defaultdict(set)

for i in range(n - 1):
    a, b = map(int, input().split())
    E[a].add(b)
    E[b].add(a)

P = [0 for _ in range(n + 1)]
P[1] = 1
Q = [1]

while len(Q) > 0:
    x = Q.pop()
    k = P[x]
    for y in E[x]:
        if P[y] == 0:
            Q.append(y)
            P[y] = -1 * k

ans0 = [i for i, p in enumerate(P) if p > 0]
ans1 = [i for i, p in enumerate(P) if p < 0]
ans = ans0[:n // 2] if len(ans0) >= len(ans1) else ans1[:n // 2]
print(*ans)
