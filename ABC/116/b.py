def find_match(a):
    for i in range(len(a) - 1):
        if a[i] == a[-1]:
            return len(a)
    return None


s = int(input())
a = [s]
i = 1
ans = 1000000
while(True):
    if a[-1] % 2 == 0:
        a.append(a[-1] // 2)
    else:
        a.append(3 * a[-1] + 1)
    x = find_match(a)
    if x is not None:
        if ans < x:
            break
        ans = x
print(ans)
