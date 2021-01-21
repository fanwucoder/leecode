from typing import List


# 2021-01-21

class UnionFoundSet:
    def init(self, n):
        # for i = 0 .. n: p[i] = i;
        p = [i for i in range(n)]
        return p

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:  # 路径压缩
            x = i
            i = p[i]
            p[x] = root
        return root


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_id = {}
        mail_name = {}
        us = UnionFoundSet()
        for account in accounts:
            name = account[0]
            for mail in account[1:]:
                mail_name[mail] = name
                if mail not in mail_id:
                    mail_id[mail] = len(mail_id)
        p = us.init(len(mail_id))
        for account in accounts:
            parent = account[1]
            for mail in account[2:]:
                us.union(p, mail_id[parent], mail_id[mail])
        import collections
        out_group = collections.defaultdict(list)
        for mail, index in mail_id.items():
            parent = us.parent(p, index)
            out_group[parent].append(mail)
        ans = [[mail_name[mails[0]]] + sorted(mails) for _, mails in out_group.items()]
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
