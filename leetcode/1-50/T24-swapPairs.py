# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        swap = ListNode(0)
        swap.next = head
        first = swap
        while swap.next != None and swap.next.next != None:
            l1 = swap.next
            l2 = l1.next
            nxt = l2.next
            l1.next = nxt
            l2.next = l1
            swap.next = l2
            swap = l1
        return first.next

