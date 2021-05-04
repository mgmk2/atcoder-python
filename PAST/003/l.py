import heapq

n = int(input())
k = [None for _ in range(n)]
t = [None for _ in range(n)]
for i in range(n):
    k[i], *t[i] = map(int, input().split())
    t[i] = t[i][::-1]
m = int(input())
a = list(map(int, input().split()))
x1 = [(-t[i].pop(), i) for i in range(n)]
x2 = [(-t[i].pop(), i) for i in range(n)]
heapq.heapify(x1)
heapq.heapify(x2)
for ai in a:
    if ai == 1:
        ans, i = heapq.heappop(x1)
        print(-ans)
        if len(t[i]) > 0:
            heapq.heappush(x1, (-t[i].pop(), i))
