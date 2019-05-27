n, m = map(int, input().split())
s = []
for i in range(m):
    si = list(map(int, input().split()))
    s.append(si)
p = list(map(int, input().split()))

ans = 0
for i in range(2 ** n):
    x = format(i, '0' + str(n) +'b')
    for j in range(m):
        q = 0
        for idx in s[j][1:]:
            if x[idx - 1] == '1':
                q += 1
        if q % 2 != p[j]:
            ans -= 1
            break
    ans += 1
print(ans)
