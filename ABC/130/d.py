n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for ai in a:
    s.append(s[-1] + ai)

ans = 0
j_pre = 0
for i in range(n + 1):
    si = s[i]
    for j in range(max(i, j_pre), n + 1):
        d = s[j] - si
        if d >= k:
            ans += n + 1 - j
            j_pre = j
            break
print(ans)
