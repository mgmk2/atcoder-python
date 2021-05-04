from fractions import gcd

K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(a, K + 1):
        for c in range(b, K + 1):
            if a == b == c:
                n = 1
            elif a == b or b == c or c == a:
                n = 3
            else:
                n = 6
            ans += n * gcd(gcd(a, b), c)
print(ans)
