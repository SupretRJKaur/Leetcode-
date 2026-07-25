# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        nodes = []
        
        # 1. Extract all values from list1
        while list1:
            nodes.append(list1.val)
            list1 = list1.next
            
        # 2. Extract all values from list2
        while list2:
            nodes.append(list2.val)
            list2 = list2.next
            
        # 3. Sort all numbers
        nodes.sort()
        
        # 4. Build a new linked list from sorted values
        dummy = ListNode(0)
        curr = dummy
        for val in nodes:
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next