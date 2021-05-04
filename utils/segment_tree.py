class SegmentTree(object):
    def __init__(self, N, func, init=0, inf=None):
        self._init_N(N)
        self._func = func
        self._inf = inf
        self._tree = [init for _ in range(2 * self._N - 1)]

    def _init_N(self, N):
        x = 1
        while x < N:
            x *= 2
        self._N = x

    def update(self, k, x):
        k += self._N - 1
        self._tree[k] = x
        while k > 0:
            k += (k - 1) // 2
            self._tree[k] = self._func(
                self._tree[2 * k + 1], self._tree[2 * (k + 1)])

    def query(self, a, b):
        ans = self._inf
        Q = [(0, 0, self._N)]

        while len(Q) > 0:
            k, l, r = Q.pop()
            if r <= a or b <= l:
                ans = self._func(ans, self._inf)
            elif a <= l and r <= b:
                ans = self._func(ans, self._tree[k])
            else:
                Q.append((2 * k + 1, l, (l + r) // 2))
                Q.append((2 * (k + 1), (l + r) // 2, r))
        return ans


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
        elif k < self._N - 1:
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
