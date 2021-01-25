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
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        size = N * N * 4
        us = UnionFind(size)
        for i in range(N):
            for j in range(N):
                idx = (i * N + j) * 4
                if grid[i][j] == '/':
                    us.unite(idx, idx + 3)
                    us.unite(idx + 1, idx + 2)
                elif grid[i][j] == '\\':
                    us.unite(idx, idx + 1)
                    us.unite(idx + 2, idx + 3)
                else:
                    us.unite(idx, idx + 1)
                    us.unite(idx, idx + 2)
                    us.unite(idx, idx + 3)

                if j + 1 < N:
                    us.unite(idx + 1, idx + 4 + 3)
                if i + 1 < N:
                    us.unite(idx + 2, idx + N * 4)
        return us.setCount


s = Solution()
print(s.regionsBySlashes([
  " /",
  "/ "
]))
print(s.regionsBySlashes([
  " /",
  "  "
]))
print(s.regionsBySlashes([
  "\\/",
  "/\\"
]))
