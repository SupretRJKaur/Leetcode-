# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root == p or root == q:
            return root
        left_report = self.lowestCommonAncestor(root.left, p, q)
        right_report = self.lowestCommonAncestor(root.right, p, q)
        if left_report is not None and right_report is not None:
            return root
        if left_report is not None:
            return left_report
        else:
            return right_report