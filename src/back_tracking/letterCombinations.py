from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['k', 'l', 'j'],
            "6": ['o', 'm', 'n'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['v', 't', 'u'],
            "9": ['w', 'x', 'y', 'z'],
        }
        ret = []
        for x in digits:
            if '2' <= x <= '9':
                letters = letter_map[x]
                ret1 = []
                if len(ret) == 0:
                    ret = ['']
                for a in ret:
                    for b in letters:
                        ret1.append(a + b)
                ret = ret1
        return ret
