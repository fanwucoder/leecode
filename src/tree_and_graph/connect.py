"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connect_tree(left, right):
            if not left:
                return left
            left.next = right
            connect_tree(left.left, left.right)
            if right:
                connect_tree(left.right, right.left)
                connect_tree(right.left, right.right)
                connect_tree(right.right, None)
            else:
                connect_tree(left.right, None)

        connect_tree(root, None)
        return root
