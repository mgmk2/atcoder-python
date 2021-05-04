n = list(map(int, list(input())))
n = n[::-1] + [0]
d = len(n)

ans = 0
for i, k in enumerate(n):
    if k < 5:
        ans += k
    elif k == 5 and n[i + 1] < 5:
        ans += k
    else:
        ans += 10 - k
        n[i + 1] += 1
print(ans)
