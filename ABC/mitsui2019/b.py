import numpy as np

n = int(input())
a = np.ceil(n / 1.08)
if int(a * 1.08) == n:
    print(int(a))
else:
    print(':(')
