# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        first_min = cur_min = ListNode(0)
        first_max = cur_max = ListNode(0)
        while head:
            if head.val < x:
                cur_min.next = head
                cur_min = cur_min.next
            else:
                cur_max.next = head
                cur_max = cur_max.next
            head = head.next

        cur_min.next = first_max.next
        cur_max.next = None
        return first_min.next

