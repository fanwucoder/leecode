# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树左子树小于根节点，右子树大于根节点，根据这个特性，中序遍历的时候，节点是按照升序遍历的，
# 记录当前遍历是第几个元素，当遍历到第k个的时候，则返回该元素。

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def getKSmallest(root, k, i_order=0):
            if not root:
                return i_order, None
            num, val = getKSmallest(root.left, k, i_order)
            if num == k:
                return k, val
            i_order = num + 1
            if i_order == k:
                return k, root.val
            i_order, val = getKSmallest(root.right, i_order, num)
            if i_order == k:
                return k, val
            return i_order, None

        _, ret = getKSmallest(root, k, 0)
        return ret
