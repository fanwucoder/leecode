import collections
from typing import List


# 1128. 等价多米诺骨牌对的数量
# 将每个多米诺骨牌的数量用hash表记录下来，每次遇到相同的，就统计一次多米诺骨牌数量
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_count = dict()
        ret = 0
        for x in dominoes:
            k = max(x) * 10 + min(x)
            ret += domino_count.get(k, 0)
            domino_count[k] = domino_count.get(k, 0) + 1
        return ret


s = Solution()
print(s.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
print(s.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6], [5, 6]]))
