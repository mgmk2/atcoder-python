z = [0 for _ in range(8)]
z[:4] = list(map(int, input().split()))
for i in range(2):
    z[2*i + 4] = z[2*i + 2] - z[2*i + 3] + z[2*i + 1]
    z[2*i + 5] = z[2*i + 3] + z[2*i + 2] - z[2*i]
print(z[4], z[5], z[6], z[7])
