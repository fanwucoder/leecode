class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        if numerator == 0:
            return '0'
        s = (numerator > 0) is (denominator > 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        ret = numerator // denominator
        res += str(ret)
        res = res if s else "-" + res
        sub = numerator % denominator
        if sub == 0:
            return res
        res += "."
        a = dict()
        a[sub] = res
        while sub != 0:
            res += str(sub * 10 // denominator)
            sub = sub * 10 % denominator
            if sub in a:
                p = res.rfind(a[sub])
                # print(p)
                res = res[:p + len(a[sub])] + "(" + res[p + len(a[sub]):] + ")"
                return res
            a[sub] = res
        return res


def test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    >>> test(1,2)
    '0.5'
    >>> test(-1,2)
    '-0.5'
    >>> test(1,3)
    '0.(3)'
    >>> test(4,333)
    '0.(012)'
    >>> test(0,3)
    '0'
    """
    s = Solution()
    return s.fractionToDecimal(*args, **kwargs)
