class FenwickTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (self.n + 1)
        for i in range(self.n):
            self.add(i + 1, data[i])

    def add(self, idx, value):
        while idx <= self.n:
            self.tree[idx] += value
            idx += idx & -idx

    def sum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

    def range_sum(self, left, right):
        return self.sum(right) - self.sum(left - 1)
