n = int(input())
a = list(map(int, input().split()))
s = sum(a)
if s % n * 2 < n:
    x = s // n
else:
    x = (s + n - 1) // n
ans = 0
for i in a:
    ans += (x - i) ** 2
print(ans)
