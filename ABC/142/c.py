n = int(input())
a = list(map(int, input().split()))
x = [(ai, i + 1) for i, ai in enumerate(a)]
x.sort()
ans = [xi[1] for xi in x]
print(*ans)
