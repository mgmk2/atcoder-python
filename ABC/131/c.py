from fractions import gcd
a, b, c, d = map(int, input().split())
cd = c * d // gcd(c, d)
xa =(a - 1) - ((a - 1) // c + (a - 1) // d - (a - 1) // cd)
xb = b - (b // c + b // d - b // cd)
print(xb - xa)
