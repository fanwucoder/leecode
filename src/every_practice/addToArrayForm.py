from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        i = 0
        cnt = len(A)
        while K != 0:
            if i < cnt:
                K += A[-(i + 1)]
                A[-(i + 1)] = K % 10
            else:
                A.insert(0, K % 10)
            K = int(K / 10)
            i += 1
        return A


s = Solution()
print(s.addToArrayForm([1, 2, 0, 0], 34))
print(s.addToArrayForm([2, 7, 4], 181))
print(s.addToArrayForm([2, 1, 5], 806))
print(s.addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1))
