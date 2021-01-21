from typing import List
import collections


# 2021-01-21

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_map = collections.defaultdict(list)
        for account in accounts:
            master = account[1]
            for mail in account[2:]:
                mail_map[mail].append(master)
                mail_map[master].append(mail)
        visit = set()
        ans = []

        def dps(graph, visited, key, result):
            if key in visited:
                return
            result.append(key)
            visited.add(key)
            for p in graph[key]:
                dps(graph, visited, p, result)

        for account in accounts:
            mails = []
            dps(mail_map, visit, account[1], mails)
            if mails:
                ans.append([account[0]] + sorted(mails))
        return ans


def main():
    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    ret = s.accountsMerge(accounts)
    print(ret)


if __name__ == '__main__':
    main()
