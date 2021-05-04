n = int(input())
s = [input() for i in range(n)]

ans = 1
for i in range(n - 1, -1, -1):
    if s[i] == 'OR':
        ans += 2 ** (i + 1)
print(ans)