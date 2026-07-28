# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def removeNthFromEnd(self, head, n):
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        total = len(nodes)
        target = total - n
        if target == 0:
            return head.next
        prevnode = nodes[target - 1]
        nextnode = nodes[target].next
        prevnode.next = nextnode
        return head