n = int(input())
a = list(map(int, input().split()))
if 0 in a:
    print(0)
else:
    ans = 1
    x = 10 ** 18
    for ai in a:
        ans *= ai
        if ans > x:
            print(-1)
            break
    else:
        print(ans)
