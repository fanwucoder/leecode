from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        cnt = len(nums)

        def backend(first, total, cur):
            if len(cur) == total:
                ret.append(cur[:])
            for i in range(first, cnt):
                cur.append(nums[i])
                first = i + 1
                backend(first, total, cur)
                cur.pop()

        for i in range(cnt + 1):
            backend(0, i, [])
        return ret
