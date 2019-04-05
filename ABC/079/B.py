n = int(input())
x = 2
y = 1
z = 1
for i in range(1, n):
    z = x + y
    x = y
    y = z
print(z)
