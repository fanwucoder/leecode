import unittest
from typing import List


# 方法一 线性查找
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        cnt = len(nums)
        if cnt == 1:
            return 0
        if cnt == 0:
            return None
        for i in range(cnt):
            if (i == 0 and nums[i] > nums[i] + 1) or (i == (cnt - 1) and nums[i] > nums[i - 1]) or (
                    nums[i - 1] < nums[i] and nums[i + 1] < nums[i]):
                return i


# 方法二
# todo 二分查找
class TestfindPeak(unittest.TestCase):
    def test_data(self):
        s = Solution()
        self.assertEqual(3, s.findPeakElement([3, 2, 1]))
        self.assertEqual(3, s.findPeakElement([1, 2, 3]))
        self.assertEqual(3, s.findPeakElement([1, 3, 2]))
        self.assertEqual(3, s.findPeakElement([1, 3]))
        self.assertEqual(3, s.findPeakElement([3, 1]))
