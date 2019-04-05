N = int(input())
L = list(map(int, input().split()))
Lm = max(L)
if 2 * Lm < sum(L):
    print('Yes')
else:
    print('No')
