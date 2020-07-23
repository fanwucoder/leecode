# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序：[1,2,4,5,3,6,7]
# 中序：[4,2,5,1,6,3,7]
#
# 		1
# 	2		3
# 4	5		6	7
#
# 整体思路，从前序遍历中取当前节点为根节点，然后根节点左边的为左子树，根节点右边的为右子树
# 1.然后获取后续的左子树边界，右边子树的边界
# 2.通过左边子树的边界，构建左子树
# 3.通过右边子树边界，构建右子树

# 0 7 0 7
# mid=3
# len1=3
# len2=3
#
# 1 4 0 3
# mid=1
# len=0
#
# 5 7 5 7

from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idx = {x: i for i, x in enumerate(inorder)}

        def build_tree(l, r, l1, r1):
            if l > r:
                return None

            root = TreeNode(preorder[l])
            mid = idx[preorder[l]]
            len1 = mid - l1 - 1
            len2 = r1 - mid

            root.left = build_tree(l + 1, l + 1 + len1, l1, mid)

            root.right = build_tree(r - len2 + 1, r, mid + 1, r1)
            return root
            # root.right = build_tree(l, r - 1, )

        return build_tree(0, len(preorder), 0, len(inorder))
