n = int(input())
x = list(map(int, input().split()))

ans = 10 ** 9
for p in range(min(x), max(x) + 1):
    cost = 0
    for xi in x:
        cost += (xi - p) ** 2
    ans = min(ans, cost)
print(ans)
