s = input()
K = int(input())
L = []
for i in range(len(s)):
    for j in range(1, K + 1):
        L.append(s[i:i + j])
L = list(set(L))
L.sort()
print(L[K - 1])
