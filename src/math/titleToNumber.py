class Solution:
    def titleToNumber(self, s: str) -> int:
        sum = 0
        cnt = 0
        for s in reversed(s):
            sum += (ord(s) - 64) * 26 ** cnt
            cnt += 1
        return sum


def test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    >>> test('A')
    1
    >>> test('AB')
    28
    >>> test('ZY')
    701
    """
    s = Solution()
    return s.titleToNumber(*args, **kwargs)
