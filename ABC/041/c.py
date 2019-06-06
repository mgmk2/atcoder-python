n = int(input())
a = list(map(int, input().split()))
t = [[a[i], i + 1] for i in range(n)]
t.sort(reverse=True)
for i in range(n):
    print(t[i][1])
