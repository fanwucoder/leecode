from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False

        def deps(board, num, i, j, used):
            ret = False
            if len(word) == num:
                return True

            if i >= len(board) or i < 0:
                return False
            if j >= len(board[0]) or j < 0:
                return False
            if used[i][j]:
                return False
            if used[i][j] is False and board[i][j] == word[num]:
                print(i, j)
                used[i][j] = True
                ret = deps(board, num + 1, i + 1, j, used)
                if not ret:
                    ret = deps(board, num + 1, i - 1, j, used)
                if not ret:
                    ret = deps(board, num + 1, i, j + 1, used)
                if not ret:
                    ret = deps(board, num + 1, i, j - 1, used)
            used[i][j] = False
            return ret

        used = [[False for _ in x] for x in board]
        for i, x in enumerate(board):
            for j in range(len(x)):
                if deps(board, 0, i, j, used):
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    a = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    b = "SEE"
    ret = s.exist(a, b)
    print(ret)
