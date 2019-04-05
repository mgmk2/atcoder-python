s = input()
xx = 1000
for i in range(len(s) - 2):
    x = int(s[i:i + 3])
    if abs(x - 753) < xx:
        xx = abs(x - 753)
print(xx)
