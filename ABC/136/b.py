s = input()
n = int(s)
m = len(s)
ans = 0
i = 1
while(True):
    if i == m:
        ans += n - 10 ** (i - 1) + 1
        break
    elif i > m:
        break
    ans += 9 * 10 ** (i - 1)
    i += 2
print(ans)
