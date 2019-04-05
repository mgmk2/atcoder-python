s = list(input())
x = list(map(int, s))
k = 0
for i in range(len(x)):
    if x[i] == 0:
        k += 1
print(2 * min(k, len(x) - k))
