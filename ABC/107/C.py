n, k = map(int, input().split())
x = list(map(int, input().split()))
t = []
for i in range(n - k + 1):
    if x[i] * x[i + k -1] >= 0:
        t.append(max(abs(x[i]), abs(x[i + k - 1])))
    else:
        t.append(x[i + k - 1] - x[i] + min(abs(x[i + k - 1]), abs(x[i])))
print(min(t))
