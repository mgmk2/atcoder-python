def dfs(i, s, l):
    if i == len(s):
        return ''
    for j in l:
        if j == int(s[i]):
            ans = dfs(i + 1, s, l)
            if ans is not None:
                ans += str(j)
                return ans
        elif j > int(s[i]):
            ans = str(l[0]) * (len(s) - i - 1) + str(j)
            return ans
    return None

n, k = map(int, input().split())
ns = str(n)
d = list(map(int, input().split()))
l = [i for i in range(10) if i not in d]
ans = dfs(0, ns, l)
if ans is None:
    if l[0] == 0:
        ans = str(l[1]) + str(l[0]) * len(ns)
    else:
        ans = str(l[0]) * (len(ns) + 1)
else:
    ans = ans[::-1]
print(ans)
