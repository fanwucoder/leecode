from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        cur = 0
        cnt = len(nums)
        last = cnt - 1
        while cur <= last:
            if nums[cur] == 2:
                nums[last], nums[cur] = nums[cur], nums[last]
                last -= 1
            if nums[cur] == 1:
                cur += 1
                continue
            if nums[cur] == 0:
                nums[first], nums[cur] = nums[cur], nums[first]
                first += 1
                cur += 1


if __name__ == '__main__':
    s = Solution()
    # a = [2, 0, 1]
    # a = [2, 0, 2, 1, 1, 0]
    a=[2,1,2]
    s.sortColors(a)
    print(a)
