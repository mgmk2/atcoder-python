n = int(input())
s = input()
ans = 0
for l in range(n):
    ss = s[l:]
    length = n - l
    i, j = 1, 0
    a = [0 for _ in range(length)]
    while i < length:
        while i + j < length and ss[j] == ss[i + j]:
            j += 1
        a[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < length and k + a[k] < j:
            a[i + k] = a[k]
            k += 1
        i += k
        j -= k
    for ll, al in enumerate(a):
        if al <= ll:
            ans = max(ans, al)
print(ans)
