from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


def test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    >>> test([10,9,2,5,3,7,101,18])
    4
    >>> test([2,5,3,7,101,18])
    4
    >>> test([10,9,2,5,3,7,101])
    4
    """
    s = Solution()

    return s.lengthOfLIS(*args, **kwargs)
