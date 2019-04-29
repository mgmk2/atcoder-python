n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
x = [0]
for ai in a:
    x.append(x[-1] + ai)

ii = 0
for i in range(n):
    for j in range(ii, n):
        if x[j + 1] - x[i] >= k:
            ii = j + 1
            break
print(max(0, n - ii))
