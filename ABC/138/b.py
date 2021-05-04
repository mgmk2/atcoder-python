n = int(input())
a = list(map(int, input().split()))
x = 0
for i in range(n):
    x += 1 / a.pop()
print(1 / x)
