from collections import defaultdict, deque

n, m = map(int, input().split())
E = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
s = int(input())
k = int(input())
t = list(map(int, input().split()))
flag = [False for _ in range(n + 1)]

Q = deque([(0, s, 0)])
while len(Q) > 0:
    count, u, num_t = Q.popleft()
    print(E[u])
    for v in E[u]:
        if v in t and num_t + 1 == k:
            break
        if flag[v]:
            continue
        flag[v] = True
        Q.append((count + 1, v, num_t + 1))
    else:
        print(Q)
        continue
    break
print(count + 1)
