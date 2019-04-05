n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a_str = [bin(a[i])[2:] for i in range(n)]
k_str = bin(k)[2:]
maxlen = min([len(a_str[-1]) + 1, len(k_str)])
x = [0 for i in range(maxlen)]
for i in range(n):
    for j in range(len(a_str[i])):
        x[j] += int(a_str[i][-j-1])
y = [min([x[i], n - x[i]]) for i in range(maxlen)]

ans = ''
for i in range(maxlen):
    if x[i] > (n + 1) // 2:
        ans = '0' + ans
    else:
        ans = '1' + ans

if k < int(ans, 2):
    idx = [[i, y[i]] for i in range(maxlen)]
    idx = sorted(idx, key=lambda x:x[1])
    idx = [idx[i][0] for i in range(maxlen)]
    i = 0
    while(True):
        tmp = list(ans)
        tmp[idx[-(i + 1)]] = str(1 - int(tmp[idx[-(i + 1)]]))
        tmp = ''.join(tmp)
        if k < int(tmp, 2):
            i += 1
        else:
            ans = tmp
            break
f = 0
for i in range(n):
    f += int(ans, 2) ^ a[i]
print(f)
