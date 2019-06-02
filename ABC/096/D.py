def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
            break
    return True

n = int(input())
x = 11
ans = []
while(True):
    if is_prime(x) and x % 5 == 1:
        ans.append(x)
        if len(ans) == n:
            break
    x += 2
print(*ans)
