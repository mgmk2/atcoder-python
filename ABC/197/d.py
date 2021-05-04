import numpy as np

n = int(input())
x0, y0 = map(int, input().split())
xn_2, yn_2 = map(int, input().split())

p0 = np.array([x0, y0], dtype=float)
pn_2 = np.array([xn_2, yn_2], dtype=float)
c = (p0 + pn_2) / 2
z0 = p0 - c

theta = 2 * np.pi / n
A = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]], dtype=float)
z1 = np.dot(A, z0)
p1 = z1 + c
print(p1[0], p1[1])