s = list(input())
x = list(map(int, s))
i = 0
ans = 0
k = 0
if len(x) == 1:
    print(0)
else:
    while(True):
        if x[i] + x[i + 1] == 1:
            k += 1
            del x[i + 1], x[i]
        if i + 2 >= len(x):
            if k == 0 or len(x) <= 1:
                break
            k = 0
            i = 0
            ans += k
        else:
            i += 1
    print(ans * 2)
