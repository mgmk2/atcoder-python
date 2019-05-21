x = int(input())
t = 2 * (x // 11)
x = x % 11
if x > 6:
    print(t + 2)
elif x > 0:
    print(t + 1)
else:
    print(t)
