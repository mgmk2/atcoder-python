n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(n // 2)] + a[n // 2:]
for i in range(n // 2 - 1, -1, -1):
    b[i] = abs(a[i] - sum(b[i::i + 1]) % 2)
print(sum(b))
print(*([i + 1 for i, bi in enumerate(b) if bi > 0]))
