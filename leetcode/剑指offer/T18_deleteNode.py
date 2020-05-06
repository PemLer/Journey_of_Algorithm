# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        first = ListNode(-1)
        first.next = head
        dummy = first

        while head:
            if head.val == val:
                first.next = head.next
                break
            head = head.next
            first = first.next
        return dummy.next