# 解法一
# 排序取第k个
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums=sorted(nums)
#         return nums[-k]
# 解法二 快速选择法
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        def find_k(start, end):
            p = random.randint(start, end)
            nums[p], nums[start] = nums[start], nums[p]
            i = start + 1
            j = end
            while i < j:
                while nums[i] > nums[start] and i < j:
                    i += 1
                while nums[j] < nums[start] and i < j:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            if nums[j] > nums[start]:
                nums[j], nums[start] = nums[start], nums[j]
            elif nums[j] < nums[start]:
                j -= 1
                nums[j], nums[start] = nums[start], nums[j]
            if j + 1 == k:
                return nums[j]
            if j + 1 < k:
                return find_k(j, end)
            if j + 1 > k:
                return find_k(start, j-1)

        return find_k(0, len(nums) - 1)

# 方法三
# 最小堆排序法
if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([99,99], 1))
