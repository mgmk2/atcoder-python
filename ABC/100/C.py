N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    x = a[i]
    while(True):
        if x % 2 == 0:
            x /= 2
            ans += 1
        else:
            break
print(ans)
