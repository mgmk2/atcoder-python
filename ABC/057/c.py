n = int(input())
x = int(n ** 0.5 + 1)
while(True):
    if n % x == 0:
        a = x
        b = n // x
        break
    else:
        x -= 1
print(max(len(str(a)), len(str(b))))
