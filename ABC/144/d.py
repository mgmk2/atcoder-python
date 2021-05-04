import numpy as np

a, b, x = map(int, input().split())
h = x / a ** 2
if 2 * h < b:
    c = 2 * x / (a * b)
    rad = np.arctan(b / c)
else:
    rad = np.arctan(2 * (b - h) / a)
print(rad * 180 / np.pi)
