n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
ai = [n for _ in range(n)]
ci = [n for _ in range(n)]
jj = 0
for i in range(n):
    for j in range(jj, n):
        if b[i] > a[j]:
            ai[i] = n - j
            break
    jj = j
ans = 0
jj = 0
for i in range(n):
    for j in range(jj, n):
        if b[i] > c[j]:
            ci[i] = n - j
            break
    jj = j
for i in range(n):
    ans += ai[i] * ci[i]
print(ans)
