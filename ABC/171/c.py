n = int(input())
x = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
while True:
    ans = x[(n - 1) % 26] + ans
    n -= 1
    n //= 26
    if n == 0:
        break
    elif n < 26:
        ans = x[n - 1] + ans
        break
print(ans)
