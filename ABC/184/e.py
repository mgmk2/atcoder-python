from collections import defaultdict, deque

def bfs(pos, a, M, E):
    u, v = pos
    M[(u, v)] = 1
    Q = deque([(u, v, 0)])
    diffs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while Q:
        u, v, d = Q.popleft()
        for du, dv in diffs:
            pos_next = (u + du, v + dv)
            c = a[pos_next]
            if c == 'G':
                return d + 1
            if c == '#':
                continue

            if M[pos_next] == 0:
                M[pos_next] = 1
                Q.append((*pos_next, d + 1))
                if c != '.':
                    E[c].discard(pos_next)

        c = a[(u, v)]
        if c.islower():
            Q += [(eu, ev, d + 1) for eu, ev in E[c]]
            E[c].clear()
    return -1

def main():
    h, w = map(int, input().split())
    a = defaultdict(lambda: '#')
    for i in range(1, h + 1):
        row = list(input())
        for j in range(1, w + 1):
            a[(i, j)] = row[j - 1]
    M = defaultdict(int)
    E = defaultdict(set)
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if a[(i, j)] == 'S':
                start = (i, j)
            elif a[(i, j)].islower():
                E[a[(i, j)]].add((i, j))

    ans = bfs(start, a, M, E)
    print(ans)

main()
