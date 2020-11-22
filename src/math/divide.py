class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        s = (dividend > 0) is (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend == 0:
            return 0

        def my_divide(a, b):
            if a < b:
                return 0
            cur = b
            m = 1
            while cur + cur < a:
                cur += cur
                m += m

            return m + my_divide(a - cur, b)

        res = my_divide(dividend, divisor)
        res = res if s else -res
        MIN_INT, MAX_INT = -2147483648, 2147483647  # [−2**31, 2**31−1]
        if res < MIN_INT:  # 根据是否溢出返回结果
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT


def test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    >>> test(10,3)
    3
    >>> test(7,-3)
    -2
    >>> test(2147483647,1)
    2147483647
    """

    s = Solution()
    return s.divide(*args, **kwargs)


