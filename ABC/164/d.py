s = input()[::-1]
l = len(s)
x = [0 for _ in range(2019)]
x[0] += 1
k = 0
p = 1
for si in s:
    k += int(si) * p % 2019
    k %= 2019
    x[k] += 1
    p *= 10
    p %= 2019

ans = 0
for xi in x:
    ans += max(0, xi * (xi - 1) // 2)
print(ans)
