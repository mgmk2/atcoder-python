x = int(input())
a = x // 100
b = x % 100
y = 5
c = []
while(b > 0 or y > 0):
    c.append(b // y)
    b = b % y
    y -= 1
print(int(sum(c) <= a))
