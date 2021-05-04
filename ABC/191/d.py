import math

x, y, r = map(float, input().split())
x = round(x * 1000)
y = round(y * 1000)
r = round(r * 1000)
# (x - a) ** 2 + (y - b) ** 2 <= r

ans = 0

left = (x - r) // 1000 * 1000
right = (x + r + 999) // 1000 * 1000
b = y // 1000 * 1000
while b >= x - r and left <= right:
    while (x - left) ** 2 + (y - b) ** 2 > r ** 2 and left <= right:
        left += 1000
    while (x - right) ** 2 + (y - b) ** 2 > r ** 2 and left <= right:
        right -= 1000
    if left <= right:
        ans += (right - left) // 1000 + 1
    b -= 1000

left = (x - r) // 1000 * 1000
right = (x + r + 999) // 1000 * 1000
b = (y + 999) // 1000 * 1000
while b <= x + r and left <= right:
    while (x - left) ** 2 + (y - b) ** 2 > r ** 2 and left <= right:
        left += 1000
    while (x - right) ** 2 + (y - b) ** 2 > r ** 2 and left <= right:
        right -= 1000
    if left <= right:
        ans += (right - left) // 1000 + 1
    b += 1000

if y % 1000 == 0:
    left = (x - r) // 1000 * 1000
    right = (x + r + 999) // 1000 * 1000
    ans -= max(0, (right - left) // 1000 + 1)
print(ans)