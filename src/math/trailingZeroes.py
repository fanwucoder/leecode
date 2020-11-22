# 检查数字中有多少个5
# 已经检查过的是否可以不检查
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # z_cnt = 0
        # for i in range(5, n + 1, 5):
        #     a = 5
        #     while i % a == 0:
        #         z_cnt += 1
        #         a *= 5
        # return z_cnt
        # n_cnt = n // 5
        # if n_cnt == 0:
        #     return 0
        # return n_cnt * (n_cnt + 1) // 2
        zero_cnt = 0
        while n > 0:
            n //= 5
            zero_cnt += n
        return zero_cnt
