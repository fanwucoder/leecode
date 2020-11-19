class Solution:
    def myPow(self, x: float, n: int) -> float:
        """

        :param x:
        :param n:
        :return:
        """
        sy = n < 0

        if n == 0:
            return 1
        if n == 1:
            return x
        n = abs(n)
        y = self.myPow(x, n // 2)
        if n % 2 == 0:
            ret = y * y
        else:
            ret = y * y * x
        return 1 / ret if sy else ret


def test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    >>> test(2,10)
    1024
    >>> test(2,0)
    1
    >>> test(2,-1)
    0.5

    """

    s = Solution()
    return s.myPow(*args, **kwargs)
