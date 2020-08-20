from typing import List

import unittest


# 寻找有序数组元素的左右边界
# 1.线性查找
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         cnt = len(nums)
#         ret = []
#         a = -1
#         for i in range(cnt):
#             if nums[i] == target:
#                 a = i
#                 break
#         if a < cnt:
#             ret.append(a)
#         a = -1
#
#         for i in reversed(range(cnt)):
#             if nums[i] == target:
#                 a = i
#                 break
#         ret.append(a)
#         return ret


# 方法2
# 二分查找
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search_left(left, right):
            while left < right:
                mid = left + int((right - left) / 2)
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                elif nums[mid] == target:
                    right = mid
            if left >= len(nums) or nums[left] != target:
                return -1
            return left

        def search_right(left, right):
            if len(nums) == 0:
                return -1
            while left < right:
                mid = left + int((right - left) / 2)
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
                elif nums[mid] == target:
                    left = mid + 1
            if left <= 0 or nums[left - 1] != target:
                return -1
            return left - 1

        a = search_left(0, len(nums))
        return [a,search_right(a, len(nums)) ]


class TestSolution(unittest.TestCase):
    def testAll(self):
        s = Solution()
        self.assertListEqual([-1, -1], s.searchRange([], 4))
        self.assertListEqual([-1, -1], s.searchRange([1, 2, 3], 4))
        self.assertListEqual([1, 2], s.searchRange([1, 2, 2, 3], 2))
        self.assertListEqual([0, 1], s.searchRange([2, 2, 3], 2))
        self.assertListEqual([1, 2], s.searchRange([1, 2, 2], 2))
        self.assertListEqual([0, 1], s.searchRange([2, 2], 2))
