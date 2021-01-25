# -*- coding: utf-8 -*-
import collections
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = len(nums)
        max_len = min(1, count)
        j = 0
        for i in range(1, count):
            if nums[i] > nums[i - 1]:
                max_len = max(max_len, i - j + 1)
            else:
                j = i
        return max_len


s = Solution()
print(s.findLengthOfLCIS([2, 2, 2, 2, 2]))
print(s.findLengthOfLCIS([1,3,5,4,7]))
