from typing import List


# 并查集模板
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def cost(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        edges = []
        count = len(points)
        dsu = UnionFind(count)
        for i in range(count):
            for j in range(i + 1, count):
                edges.append((cost(points[i], points[j]), i, j))
        edges.sort()
        ret, num = 0, 1
        for length, x, y in edges:
            if dsu.unite(x, y):
                ret += length
                num += 1
                if num == count:
                    break

        return ret


s = Solution()
print(s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20)
print(s.minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]), 4)
print(s.minCostConnectPoints([[-1000000, -1000000], [1000000, 1000000]]), 4000000)
print(s.minCostConnectPoints([[-0, -0]]), 0)
