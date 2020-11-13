from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cnt = 0
        rest = amount
        coins = sorted(coins, reverse=True)
        for i in range(len(coins)):
            if rest >= coins[i]:
                type_cnt = int(rest / coins[i])
                rest = rest % coins[i]
                cnt += type_cnt
                print(coins[i], type_cnt)
        print(rest)
        if rest > 0:
            return -1
        return cnt


"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

你可以认为每种硬币的数量是无限的。
示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2

暂时想到1中暴力方法，尝试每种面额的的取值范围，一次组合，比如例1中，面额"1"的有11种选择，面额"2"五种，面额"5"的有2两种，总的尝试次数就是11*2*5
"""


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def sub_change(coins, p, cur, cnt):
            # print(p, cur, cnt)
            if amount == cur:
                return cnt
            if p >= len(coins):
                return -1
            step = coins[p]
            small_cnt = -1
            for i in range(int(amount / step) + 1):
                if small_cnt == -1:
                    small_cnt = sub_change(coins, p + 1, cur + i * step, cnt + i)
                else:
                    a = sub_change(coins, p + 1, cur + i * step, cnt + i)
                    small_cnt = small_cnt if a == -1 else min(a, small_cnt)
                # if small_cnt == 3:
                #     print("-----------")
            return small_cnt

        return sub_change(coins, 0, 0, 0)


import functools


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @functools.lru_cache(amount)
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return -1
            min_coins = -1
            for c in self.coins:
                res = dp(rem - c)
                if res == -1:
                    pass
                else:
                    if min_coins == -1:
                        min_coins = res + 1
                    else:
                        min_coins = min(res + 1, min_coins)
            return min_coins

        self.coins = coins
        if amount == 0: return 0
        return dp(amount)


def test(*argc, **kwargs):
    """

    :param argc:
    :param kwargs:
    :return:

    >>> test([1,2,5],11)
    3
    >>> test([2],3)
    -1
    >>> test([1],0)
    0
    >>> test([1],1)
    1
    >>> test([1],2)
    2
    >>> test([186,419,83,408],6249)
    20
    """
    s = Solution2()
    return s.coinChange(*argc, **kwargs)


# test([186, 419, 83, 408], 6249)
print(test([1, 2, 5], 11))
