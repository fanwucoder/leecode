from typing import List
import sys


class Solution1:
    def maximumProduct(self, nums: List[int]) -> int:
        max1 = max2 = max3 = -sys.maxsize - 1

        min1 = min2 = sys.maxsize

        # print(max1, max2, max3, min1, min2)
        for x in nums:
            if x > max3:
                if x > max1:
                    max3 = max2
                    max2 = max1
                    max1 = x
                elif x > max2:
                    max3 = max2
                    max2 = x
                elif x > max3:
                    max3 = x
            if x < min2:
                if x < min1:
                    min2 = min1
                    min1 = x
                elif x < min2:
                    min2 = x
            # print(max1, max2, max3, min1, min2)
        return max(max1 * max2 * max3, max1 * min2 * min1)


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        # print((nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1]))
        a, b = nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1]
        return max(a,b)


s = Solution()
print(s.maximumProduct([1, 2, 3]))
print(s.maximumProduct([1, 2, 3, 4]))
print(s.maximumProduct([-1, -2, -3, 6]))
print(s.maximumProduct([1000, 1, 1, 1]))
