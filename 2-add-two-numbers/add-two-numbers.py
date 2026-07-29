# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        arr1 = []
        while l1:
            arr1.append(l1.val)
            l1 = l1.next

        arr2 = []
        while l2:
            arr2.append(l2.val)
            l2 = l2.next

        res_arr = []
        carry = 0
        i = 0

        while i < len(arr1) or i < len(arr2) or carry:
            v1 = arr1[i] if i < len(arr1) else 0
            v2 = arr2[i] if i < len(arr2) else 0

            total = v1 + v2 + carry
            carry = total // 10
            res_arr.append(total % 10)
            i = i+ 1

        head = ListNode(res_arr[0])
        curr = head

        for val in res_arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return head