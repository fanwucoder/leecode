# class Solution(object):
#     def canJump(self, nums):
#         """
#         不行，这个是穷举法
#         :type nums: List[int]
#         :rtype: bool
#         """
#         howto = [0] * len(nums)
#         rest = [x for x in nums]
#         start = 0
#         finish = len(nums)
#         cnt = 0
#         while True:
#
#             next_start = start + rest[start]
#             if next_start >= finish - 1:
#                 return True
#             if start == 0 and rest[0] == 0:
#                 return False
#             howto[next_start] = rest[start]
#             rest[start] -= 1
#             start = next_start
#
#             # print("start:%s" % start)
#             # print("howto:%s" % howto)
#             # print("rest:%s" % rest)
#             # print()
#             while rest[start] == 0:
#                 start = start - howto[start]
#                 if start == 0 and rest[0] == 0:
#                     return False
#         return False


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
from typing import List


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         step = 0
#         how = [x for x in nums]
#         word=[]
#         stop = len(nums)
#         while True:
#             if step == 0 and how[step] == 0:
#                 break
#             next_step = step + how[step]
#             if next_step >= stop:
#                 return True
#             # 1.不能走路，回退
#             if how[next_step] == 0:
#                 if how[step] == 0:
#                     step -= 1
#                 else:
#                     how[step] -= 1
#             # 2.可以走
#             else:
#                 step = next_step
#
#         return False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        rightmost = 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
            if rightmost >= n - 1:
                return True
        return False


def test(*args, **kwargs):
    """

    Args:
        *args:
        **kwargs:

    Returns:
    >>> test([2,3,1,1,4])
    True
    >>> test( [3,2,1,0,4])
    False
    >>> test([0])
    True
    >>> test([0,1])
    :return:
    >>> test([2,3,1,1,4])
    True
    >>> test([3,2,1,0,4])
    False
    >>> test([3,2,2,0,4])
    True
    >>> test([])
    False
    """
    s = Solution()
    return s.canJump(*args, **kwargs)
