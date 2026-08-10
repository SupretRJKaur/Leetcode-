# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        numbers = []
        def collect_numbers(node):
            if node is None:
                return
            collect_numbers(node.left)
            numbers.append(node.val) 
            collect_numbers(node.right)
        collect_numbers(root)
        return numbers[k - 1]