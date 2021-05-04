n, m = map(int, input().split())
s = input()
s = s[::-1]
idx = 0
ans = []
while(True):
    d = s[idx + 1:idx + m + 1].rfind('0')
    if d == -1:
        print(-1)
        break
    ans.append(d + 1)
    idx += d + 1
    if idx == n:
        print(*ans[::-1])
        break
