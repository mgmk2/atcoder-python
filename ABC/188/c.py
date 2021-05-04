import numpy as np

n = int(input())
a = list(map(int, input().split()))
winner = np.argmax(a)
ans = 1
center = 2 ** (n - 1)
if winner < center:
    ans += center + np.argmax(a[center:])
else:
    ans += np.argmax(a[:center])
print(ans)