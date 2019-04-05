n = int(input())
a = list(map(int, input().split()))
ans = 0
while(True):
    for i in range(n):
        if a[i] % 2:
            print(ans)
            exit()
        else:
            a[i] = a[i] // 2
    ans += 1
