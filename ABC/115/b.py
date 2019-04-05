n = int(input())
x = 0
y = 0
for i in range(n):
    p = int(input())
    if p > x:
        x = p
    y += p
print(y - x // 2)
