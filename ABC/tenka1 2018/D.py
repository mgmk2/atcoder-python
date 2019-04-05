N = int(input())
k = int((2 * N) ** 0.5) + 1
if k * (k - 1) == 2 * N:
    print('Yes')
    a = range(1, k)
    S = [[1]]
    for i in range(1, k - 1):
        S[0].append(S[0][-1] + i)
    for i in range(1, k - 1):
        S.append(list(range(S[0][i], S[0][i] + i + 1)))
        for j in range(i + 1, k - 1):
            S[-1].append(S[-1][-1] + j)
    S.append([1])
    for i in range(2, k):
        S[-1].append(S[-1][-1] + i)
    for i in range(k):
        print(' '.join(map(str, [k - 1] + S[i])))
else:
    print('No')
