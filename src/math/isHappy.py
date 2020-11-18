class Solution:
    def isHappy(self, n: int) -> bool:
        is_repeat = set()
        total = n
        is_repeat.add(total)
        while total != 1:
            total1 = 0
            for s in str(total):
                s = int(s)
                total1 += s * s
            total = total1
            if total in is_repeat:
                return False
            is_repeat.add(total1)
            total = total1
            print(total)
        return True


s = Solution()
print(s.isHappy(19))
