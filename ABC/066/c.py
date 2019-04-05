n = int(input())
a = list(map(int, input().split()))
a1 = a[::2]
a2 = a[1::2]
if n % 2 == 0:
    ans = a2[::-1] + a1
else:
    ans = a1[::-1] + a2
print(*ans)
