class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _update_range(self, idx, l, r, ul, ur, val):
        if self.lazy[idx] != 0:
            self.tree[idx] += (r - l + 1) * self.lazy[idx]
            if l != r:
                self.lazy[idx * 2] += self.lazy[idx]
                self.lazy[idx * 2 + 1] += self.lazy[idx]
            self.lazy[idx] = 0
        if ul > r or ur < l:
            return
        if ul <= l and ur >= r:
            self.tree[idx] += (r - l + 1) * val
            if l != r:
                self.lazy[idx * 2] += val
                self.lazy[idx * 2 + 1] += val
            return
        mid = (l + r) // 2
        self._update_range(idx * 2, l, mid, ul, ur, val)
        self._update_range(idx * 2 + 1, mid + 1, r, ul, ur, val)
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]

    def _query_range(self, idx, l, r, ql, qr):
        if self.lazy[idx] != 0:
            self.tree[idx] += (r - l + 1) * self.lazy[idx]
            if l != r:
                self.lazy[idx * 2] += self.lazy[idx]
                self.lazy[idx * 2 + 1] += self.lazy[idx]
            self.lazy[idx] = 0
        if ql > r or qr < l:
            return 0
        if ql <= l and qr >= r:
            return self.tree[idx]
        mid = (l + r) // 2
        return self._query_range(idx * 2, l, mid, ql, qr) + self._query_range(idx * 2 + 1, mid + 1, r, ql, qr)

    def update(self, ul, ur, val):
        self._update_range(1, 1, self.n, ul, ur, val)

    def query(self, ql: int, qr: int) -> int:
        return self._query_range(1, 1, self.n, ql, qr)
