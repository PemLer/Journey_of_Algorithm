# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(head2)
        return self.merge_sort(left, right)
    
    def merge_sort(self, left, right):
        first = new = ListNode(-1)
        while left and right:
            if left.val < right.val:
                new.next = left
                left = left.next
            else:
                new.next = right
                right = right.next
            new = new.next
        if left:
            new.next = left
        if right:
            new.next = right
        return first.next
        
