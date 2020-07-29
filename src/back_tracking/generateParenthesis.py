from functools import lru_cache
from typing import List


class Solution:
    @lru_cache
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        ans = []
        for c in range(n):
            for a in self.generateParenthesis(c):
                for b in self.generateParenthesis(n - 1 - c):
                    ans.append("({}){}".format(a, b))
        return ans
