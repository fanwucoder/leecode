class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def search_data(nums, target):
            lower = 0
            higher = len(nums)
            while lower < higher:
                mid = int((lower + higher) / 2)
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    higher = mid
                elif nums[mid] < target:
                    lower = mid + 1

        for nums in matrix:
            if len(nums) == 0:
                return False
            if nums[0] <= target <= nums[-1] and search_data(nums, target):
                return True
            if nums[0] > target:
                return False
        return False


def test(*args, **kwargs):
    """

    :return:
    >>> test([[1,   4,  7, 11, 15],
    ... [2,   5,  8, 12, 19],
    ...   [3,   6,  9, 16, 22],
    ...   [10, 13, 14, 17, 24],
    ...   [18, 21, 23, 26, 30]
    ... ],5)
    True
    >>> test([
    ... [1,   4,  7, 11, 15],
    ... [2,   5,  8, 12, 19],
    ...   [3,   6,  9, 16, 22],
    ...   [10, 13, 14, 17, 24],
    ...   [18, 21, 23, 26, 30]
    ... ],20)
    False
    """
    s = Solution()
    return s.searchMatrix(*args, **kwargs)
