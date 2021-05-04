n = int(input())
b = list(map(int, input().split()))
a = [10 ** 9 for _ in range(n)]
for i, bi in enumerate(b):
    a[i] = min(a[i], bi)
    a[i + 1] = bi
print(sum(a))
