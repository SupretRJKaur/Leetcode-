# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def hasCycle(self, head):
        slow = head
        fast = head

        # Keep running as long as fast pointer and its next node exist
        while fast and fast.next:
            slow = slow.next  # Move 1 step
            fast = fast.next.next  # Move 2 steps

            # If they meet at the exact same node, there's a cycle!
            if slow == fast:
                return True

        # If fast reaches the end (None), there's no cycle
        return False