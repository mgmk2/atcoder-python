n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0]
for ai in a:
    b.append(b[-1] + ai)
ans = 0
for i in range(n - k + 1):
    ans += b[i + k] - b[i]
print(ans)
