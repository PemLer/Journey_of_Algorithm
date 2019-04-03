# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = ListNode(0)
        first = cur
        while head != None:
            if head.val != val:
                cur.next = ListNode(head.val)
                head = head.next
                cur = cur.next
            else:
                head = head.next
                #cur = head.next
                # cur = cur.next
        return first.next

