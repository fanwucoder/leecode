from typing import List
from collections import defaultdict
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = defaultdict(int)
        b = defaultdict(int)
        q = []
        for s in tasks:
            a[s] += 1
            b[s] = -n
        for k, v in a.items():
            heapq.heappush(q, (10 * 100, k))
        cnt = 0
        # print(b)
        while q:
            p, s = heapq.heappop(q)

            if (cnt - b[s]) < n:
                res = n - (cnt - b[s])
                cnt += res
            a[s] -= 1
            cnt += 1
            # print(a, b, s,q, cnt)
            if a[s] <= 0:
                a.pop(s)
            else:
                b[s] = cnt
                heapq.heappush(q, (p + cnt, s))

        return cnt


def test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    >>> test( ["A","A","A","B","B","B"],2)
    8
    >>> test( ["A","A","A","B","B","B","c","c","c"],2)
    9
    >>> test( ["A","A","A","B","B","B","c","c","c","c"],2)
    12
    """

    s = Solution()
    return s.leastInterval(*args, **kwargs)
