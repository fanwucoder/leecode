# 1489. 找到最小生成树里的关键边和伪关键边

# 并查集模板
from typing import List


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
        # 用于优化的，减少路径压缩次数的
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        us = UnionFind(n)
        edges.sort(key=lambda x: x[2])
        values = 0
        m = len(edges)
        for i in range(m):
            if us.unite(edges[i][0], edges[i][1]):
                values += edges[i][2]
        ans = [list(), list()]
        for i in range(m):
            v = 0
            us1 = UnionFind(n)
            for j in range(m):
                if i != j and us1.unite(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if us1.setCount != 1 or (us1.setCount == 1 and v > values):
                # print(i, us1.setCount, v, values)
                ans[0].append(edges[i][3])
                continue

            us1 = UnionFind(n)
            us1.unite(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i != j and us1.unite(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == values:
                # print(i, us1.setCount, v, values)
                ans[1].append(edges[i][3])
        return ans


class Solution1:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x: x[2])

        # 计算 value
        uf_std = UnionFind(n)
        value = 0
        for i in range(m):
            if uf_std.unite(edges[i][0], edges[i][1]):
                value += edges[i][2]

        ans = [list(), list()]

        for i in range(m):
            # 判断是否是关键边
            uf = UnionFind(n)
            v = 0
            for j in range(m):
                if i != j and uf.unite(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if uf.setCount != 1 or (uf.setCount == 1 and v > value):
                print('a',i, uf.setCount, v, value,edges[i][3])
                ans[0].append(edges[i][3])
                continue

            # 判断是否是伪关键边
            uf = UnionFind(n)
            uf.unite(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i != j and uf.unite(edges[j][0], edges[j][1]):
                    v += edges[j][2]
            if v == value:
                print('b',i, uf.setCount, v, value,edges[i][3])
                ans[1].append(edges[i][3])

        return ans


s = Solution()
print(s.findCriticalAndPseudoCriticalEdges(6, [[0, 1, 1], [1, 2, 1], [0, 2, 1], [2, 3, 4], [3, 4, 2], [3, 5, 2],
                                               [4, 5, 2]]))
