# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = Queue()
        q.put(root)
        ele = []
        while not q.empty():
            e = q.get()
            if e is None:
                ele.append(e)
            else:
                ele.append(e.val)
                q.put(e.left)
                q.put(e.right)
        while len(ele) > 0:
            if not ele[-1]:
                ele.pop()
            else:
                break
        return str(ele)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data=data.replace('null','None')
        arr = eval(data)

        q = Queue()
        for x in arr:
            q.put(x)
        build_q = Queue()
        if q.empty():
            return None
        root_val = q.get()
        if not root_val:
            return None
        root = TreeNode(root_val)
        build_q.put(root)
        while not q.empty() and not build_q.empty():
            e = q.get()
            node = build_q.get()
            print(node.val)
            if e:
                node.left = TreeNode(e)
                build_q.put(node.left)
            else:
                node.left = e
            if q.empty():
                break
            e = q.get()
            if e:
                node.right = TreeNode(e)
                build_q.put(node.right)
            else:
                node.right = e

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "%s,%s,%s" % (self.val, self.left, self.right)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(5)
# ser = Codec()
# print(ser.serialize(root))

# deser = Codec()
# root = deser.deserialize('[1, 2, 3, None, None, 4, 5, None, None, None, None]')
# print(root)

deser = Codec()
root = deser.deserialize(
    '[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]')
print(root)


def test(*args, **kwargs):
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(*args, **kwargs))
    return ans
