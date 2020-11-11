from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        step = 0
        how = [x for x in nums]
        word=[]
        stop = len(nums)
        while True:
            if step == 0 and how[step] == 0:
                break
            next_step = step + how[step]
            if next_step >= stop:
                return True
            # 1.不能走路，回退
            if how[next_step] == 0:
                if how[step] == 0:
                    step -= 1
                else:
                    how[step] -= 1
            # 2.可以走
            else:
                step = next_step

        return False


def test(*args, **kwargs):
    """

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
