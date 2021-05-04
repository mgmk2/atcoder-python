n = int(input())
a = [set(input()) for i in range(n)]
ans = ''
for i in range(n // 2):
    x = a[i] & a[-(i + 1)]
    if len(x) == 0:
        print(-1)
        break
    ans += x.pop()
else:
    if n % 2:
        print(ans + a[n // 2].pop() + ans[::-1])
    else:
        print(ans + ans[::-1])
