from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

n = int(input())
t = int(input())
for i in range(n - 1):
    t = lcm(t, int(input()))
print(t)
