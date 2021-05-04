n = int(input())
a = list(map(int, input().split()))
ans = [0 for _ in range(n)]

for i in range(n - 2, -1, -1):
    ans[a[i] - 1] += 1
for x in ans:
    print(x)
