n = int(input())
t = list(map(int, input().split()))
T = sum(t)
m = int(input())
ans = []
for i in range(m):
    p, x = map(int, input().split())
    ans.append(T - t[p - 1] + x)
for a in ans:
    print(a)
