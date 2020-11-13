class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0 for j in range(n)] for i in range(m)]
        path[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    path[i][j] = 1
                elif i == 0:
                    path[i][j] = 0 + path[i][j - 1]
                elif j == 0:
                    path[i][j] = path[i - 1][j] + 0
                else:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]
                # print(i, j, path[i][j])
        return path[m - 1][n - 1]


def test(*argc, **kwargs):
    """

    :param argc:
    :param kwargs:
    :return:

    >>> test(m=7,n=3)
    28
    >>> test(m=3,n=2)
    3
    """
    s = Solution()
    return s.uniquePaths(*argc, **kwargs)


print(test(7, 3))
