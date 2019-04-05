def search(s, m, n, bridge):
    c = [1]
    d = [1]
    for k in range(n):
        cc = []
        for i, ci in enumerate(c):
            tmp = []
            for j in range(m):
                if j == bridge:
                    continue
                elif s[j][0] == ci and s[j][1] not in d:
                    tmp.append(s[j][1])
                elif s[j][1] == ci and s[j][0] not in d:
                    tmp.append(s[j][0])
            cc += tmp
            d += tmp
        if cc == []:
            break
        else:
            c = cc
    if len(d) == n:
        return 0
    else:
        return 1

n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
ans = 0
for i in range(m):
    ans += search(s, m, n, i)
print(ans)
