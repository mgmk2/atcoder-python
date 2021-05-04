x = int(input())
k = 100
y = 0
while k < x:
    k *= 1.01
    k = int(k)
    y += 1
print(y)
