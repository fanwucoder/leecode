from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def b_search(nums, l, h):
            if l >= h:
                return -1
            mid = int((l + h) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[min(h, len(nums) - 1)]:
                if nums[l] <= target <= nums[mid]:
                    return b_search(nums, l, mid)
                return b_search(nums, mid + 1, h)
            else:
                if nums[mid] <= target <= nums[min(h, len(nums) - 1)]:
                    return b_search(nums, mid + 1, h)
                return b_search(nums, l, mid)

        return b_search(nums, 0, len(nums))


def test(*argc, **kwargs):
    """

    :param argc:
    :param kwargs:
    :return:

    >>> test([4,5,6,7,0,1,2],4)
    0
    >>> test([4,5,6,7,0,1,2],7)
    3
    >>> test([4,5,6,7,0,1,2],0)
    4
    >>> test([4,5,6,7,0,1,2],2)
    6
    >>> test([4,5,6,7,0,1,2],3)
    -1
    >>> test([4,5,6,7,0,1,2],5)
    1
    >>> test([4,5,6,7,0,1,2],1)
    5
    >>> test([1],0)
    -1
    >>> test([1],1)
    0
    """
    s = Solution()
    return s.search(*argc, **kwargs)
