def f(a, x):
    m = len(a)
    ans = 0
    for ai in a:
        ans = ans | ai
    if x is not None:
        ans = ans ^ x

    for i in range(1, m):
        p = 0
        for j in range(i):
            p = p | a[j]
        ans = min(ans, f(a[i:], p if x is None else p ^ x))
    
    return ans

n = int(input())
a = list(map(int, input().split()))
print(f(a, None))