n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ans = 2 * 10 ** 5
for i, ai in enumerate(a):
    for j, bj in enumerate(b):
        if i == j:
            ans = min(ans, ai + bj)
        else:
            ans = min(ans, max(ai, bj))
print(ans)
