x, y, a, b = map(int, input().split())

ans = 0

while True:
    if x * a > x + b:
        ans += (y - 1 - x) // b
        break
    elif x * a < y:
        x *= a
        ans += 1
    else:
        break
print(ans)
