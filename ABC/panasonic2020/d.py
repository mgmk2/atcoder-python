c = 'abcdefghij'

def join(s, k, n):
    if len(s) == n:
        return [s]
    ans = []
    for i in range(k):
        ans += join(s + c[i], k, n)
    ans += join(s + c[k], k + 1, n)
    return ans

n = int(input())
ans = join('', 0, n)
for x in ans:
    print(x)
