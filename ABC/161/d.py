k = int(input())
if k < 10:
    print(k)
else:
    d = [[str(i)] for i in range(10)]
    n = 9
    while True:
        dd = [None for _ in range(10)]
        dd[0] = ['0' + j for j in d[0]] + ['0' + j for j in d[1]]
        for i in range(1, 9):
            si = str(i)
            dd[i] = [si + j for j in d[i - 1]] + [si + j for j in d[i]] + [si + j for j in d[i + 1]]
            n += len(dd[i])
            if n >= k:
                break
        else:
            i += 1
            dd[9] = ['9' + j for j in d[8]] + ['9' + j for j in d[9]]
            n += len(dd[i])
        if n >= k:
            print(dd[i][k - n - 1])
            break
        d = dd
