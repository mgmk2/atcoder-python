n, k, q = map(int, input().split())
p = [0 for _ in range(n)]
for i in range(q):
    a = int(input())
    p[a - 1] += 1
for pi in p:
    if k - q + pi > 0:
        print('Yes')
    else:
        print('No')
