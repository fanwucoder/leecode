import unittest
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if len(intervals) == 0:
            return []
        ret = []
        for x in intervals:
            if not ret or x[0] > ret[-1][1]:
                ret.append(x)
            else:
                ret[-1][1] = max(ret[-1][1], x[1])
        return ret


class TestSolution(unittest.TestCase):
    def testAll(self):
        s = Solution()
        a = s.merge([[1, 2], [3, 4]])
        self.assertListEqual([[1, 2], [3, 4]], a)
        a = s.merge([[1, 2], [2, 3]])
        self.assertListEqual([[1, 3]], a)
