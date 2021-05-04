r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

d = r2 - c2 - (r1 - c1)
s = r2 + c2 - (r1 + c1)

if (r1, c1) == (r2, c2):
    ans = 0
elif s == 0 or d == 0 or abs(r2 - r1) + abs(c2 - c1) <= 3:
    ans = 1
elif s % 2 == 0 or d % 2 == 0 or min(abs(s), abs(d)) in [1, 2, 3, 5]:
    ans = 2
else:
    ans = 3
print(ans)
