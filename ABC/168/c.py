import numpy as np

a, b, h, m = map(int, input().split())
theta_h = 2 * np.pi * (h * 60 + m) / 720
theta_m = 2 * np.pi * m / 60
dx = a * np.cos(theta_h) - b * np.cos(theta_m)
dy = a * np.sin(theta_h) - b * np.sin(theta_m)
d = np.sqrt(dx ** 2 + dy ** 2)
print(d)
