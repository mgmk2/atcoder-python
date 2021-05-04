from collections import defaultdict

def bfs(i, V, E, Ec):
    V[i] = 1
    Q = [(i, 0)]
    while(True):
        Qi = []
        for q, cq in Q:
            c = 1
            for j, idx in E[q]:
                if V[j] == 0:
                    if cq == c:
                        c += 1

                    V[j] = 1
                    Qi.append((j, c))
                    Ec[idx] = c
                    c += 1
        if len(Qi) == 0:
            break
        else:
            Q = Qi
    return V, Ec


n = int(input())
E = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    E[a].append((b, i))
    E[b].append((a, i))
Ec = [None for _ in range(n - 1)]
V = [0 for _ in range(n + 1)]
_, Ec = bfs(1, V, E, Ec)
print(max(Ec))
for c in Ec:
    print(c)
