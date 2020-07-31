from typing import List


class Solution:
    """
    回溯算法的基本入门例子
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False for i in range(len(nums))]
        depth = 0
        path = []
        res = []
        self.dfs(nums, used, depth, path, res)
        return res

    def dfs(self, nums, used, depth, path, res):
        if depth == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                self.dfs(nums, used, depth + 1, path, res)
                path.pop()
                used[i] = False
