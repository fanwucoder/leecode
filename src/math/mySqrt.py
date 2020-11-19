class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = -1
        while l <= r:
            mid =(l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans


def test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    >>> test(2)
    1
    >>> test(4)
    2
    >>> test(8)
    2
    >>> test(1)
    1

    """

    s = Solution()
    return s.mySqrt(*args, **kwargs)
