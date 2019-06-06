class dijkstra(object):
    def __init__(self, start, n, E, INF=1e10):
        self.INF = INF
        self.start = start
        self.n = n
        self.V = [0 for _ in range(n + 1)]
        self.E = E
        self.d = [INF for _ in range(n + 1)]
        self.d[start] = 0

    def run(self):
        Q = [[i, self.d[i]] for i in range(1, self.n + 1)]

        while(len(Q) > 0):
            Q.sort(key=lambda x: x[1], reverse=True)
            u = Q.pop()[0]
            for v, l in self.E[u].items():
                if self.d[v] > self.d[u] + l[0]:
                    self.d[v] = self.d[u] + l[0]
                    self.V[v] = u
            Q = [[x[0], self.d[x[0]]] for x in Q]

    def count_path(self):
        def find_path(i, Qv):
            Qv[i] += 1
            if i != self.start:
                self.E[i][self.V[i]][-1] += 1
                self.E[self.V[i]][i][-1] += 1
                Qv = find_path(self.V[i], Qv)
            return Qv

        Qv = [0 for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            if i == self.start or Qv[i] > 0:
                continue
            Qv = find_path(i, Qv)

        return self.E
