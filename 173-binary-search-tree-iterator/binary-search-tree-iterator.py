# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        self.nodes = []
        self.index = -1
        # Run a full in-order traversal to flatten the entire tree into a list
        self._inorder(root)

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        self.nodes.append(node.val)
        self._inorder(node.right)

    def next(self):
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self):
        return self.index + 1 < len(self.nodes)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()