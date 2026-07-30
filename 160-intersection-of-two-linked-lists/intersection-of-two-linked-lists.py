# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        visited = set()
        curr = headA
        while curr:
            visited.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in visited:
                return curr 
            curr = curr.next
        return None