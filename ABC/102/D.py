n = int(input())
a = list(map(int, input().split()))
s = [0]
INF = 10 ** 9 + 7
for ai in a:
    s.append(s[-1] + ai)

idx = 0
for i in range(1, n - 2):
    p = INF
    idx2 = i - 1
    for j in range(idx, i):
        pp = abs(2 * s[j] - s[i + 1])
        if p <= pp:
            idx2 = j
            break
        else:
            p = pp
    idx = idx2
