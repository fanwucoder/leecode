from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cnt = len(nums)
        res = []

        for i in range(cnt + 1):
            path = []
            used = [False for x in range(cnt)]
            self.backend(i, 0, path, used, res, cnt, nums)
        return res

    def backend(self, total, begin, path, used, res, cnt, nums):
        if len(path) == total:
            res.append(path[:])
            return
        for i in range(begin, cnt):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                self.backend(total, i + 1, path, used, res, cnt, nums)
                used[i] = False
                path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
