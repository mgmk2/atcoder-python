class LazySegmentTree(object):
    def __init__(self, N, func, init=0, inf=None):
        self._init_N(N)
        self._func = func
        self._init = init
        self._inf = inf
        self._tree = [init for _ in range(2 * self._N - 1)]
        self._lazy_tree = [None for _ in range(2 * self._N - 1)]

    def _init_N(self, N):
        x = 1
        while x < N:
            x *= 2
        self._N = x

    def _eval(self, k):
        if self._lazy_tree[k] is None:
            return

        v = self._lazy_tree[k]
        if k < self._N - 1:
            self._lazy_tree[2 * k + 1] = v
            self._lazy_tree[2 * (k + 1)] = v

        self._tree[k] = v
        self._lazy_tree[k] = None

    def update(self, a, b, x):
        Q = [(0, 0, self._N, False)]

        while len(Q) > 0:
            k, l, r, can_update_tree = Q.pop()
            if can_update_tree:
                self._tree[k] = self._func(
                    self._tree[2 * k + 1], self._tree[2 * (k + 1)])
                continue

            self._eval(k)
            if a <= l and r <= b:
                self._lazy_tree[k] = x
                self._eval(k)
            elif a < r and l < b:
                Q.append((k, l, r, True))
                Q.append((2 * k + 1, l, (l + r) // 2, False))
                Q.append((2 * (k + 1), (l + r) // 2, r, False))

    def query(self, a, b):
        ans = self._inf
        Q = [(0, 0, self._N)]

        while len(Q) > 0:
            k, l, r = Q.pop()
            self._eval(k)
            if r <= a or b <= l:
                ans = self._func(ans, self._inf)
            elif a <= l and r <= b:
                ans = self._func(ans, self._tree[k])
            else:
                Q.append((2 * k + 1, l, (l + r) // 2))
                Q.append((2 * (k + 1), (l + r) // 2, r))
        return ans


w, n = map(int, input().split())
s = set()
LR = []
for i in range(n):
    l, r = map(int, input().split())
    LR.append((l, r))
    s.add(l)
    s.add(r)

s = list(s)
s.sort()
indices = {x: i for i, x in enumerate(s)}
tree = LazySegmentTree(len(s), max, init=0, inf=0)

for l, r in LR:
    ll = indices[l]
    rr = indices[r] + 1
    h = 1 + tree.query(ll, rr)
    tree.update(ll, rr, h)
    print(h)
