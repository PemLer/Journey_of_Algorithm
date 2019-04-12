# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None or head.next.next == None:
            return head
        cur = q = head.next
        p = head
        while cur and cur.next:
            cur = cur.next
            q.next = cur.next
            cur.next = p.next
            p.next = cur
            p = p.next
            q = q.next
            cur  = q
        return head


