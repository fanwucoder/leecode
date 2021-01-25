# -*- coding: utf-8 -*-
import collections
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


class Solution1:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind(n)
        for con in connections:
            uf.unite(con[0], con[1])
        total_con = len(connections)
        if total_con < n - 1:
            return -1
        print(uf.parent)
        return uf.setCount - 1


# 深度优先，更快
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        total_con = len(connections)
        if total_con < n - 1:
            return -1
        edges = collections.defaultdict(list)
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)
        seen = set()

        def dps(p):
            seen.add(p)
            for p1 in edges[p]:
                if p1 not in seen:
                    dps(p1)

        ans = 0
        for x in range(n):
            if x not in seen:
                ans += 1
                dps(x)
        return ans-1

s = Solution()
print(s.makeConnected(12,
                      [[1, 5], [1, 7], [1, 2], [1, 4], [3, 7], [4, 7], [3, 5], [0, 6], [0, 1], [0, 4], [2, 6], [0, 3],
                       [0, 2]]))
