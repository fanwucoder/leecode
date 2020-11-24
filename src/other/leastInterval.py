from typing import List
from collections import defaultdict
import heapq


class Solution1:
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


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = [0 for i in range(26)]
        for s in tasks:
            a[ord(s) - ord('A')] += 1
        a=sorted(a)
        max_val = a[25] - 1
        # print(a)
        total = max_val * n
        i = 24
        while i >= 0 and a[i] > 0:
            total -= min(max_val, a[i])
            i -= 1
        return total + len(tasks) if total > 0 else len(tasks)


def test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    >>> test( ["A","A","A","B","B","B"],2)
    8
    >>> test( ["A","A","A","B","B","B","C","C","C"],2)
    9
    >>> test( ["A","A","A","B","B","B","C","C","C","C"],2)
    10
    """

    s = Solution()
    return s.leastInterval(*args, **kwargs)
