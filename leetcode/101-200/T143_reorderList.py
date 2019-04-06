# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pre = ListNode(-1)
        pre.next = head
        slow = fast = pre
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        second = self.reverse_list(second)
        while second:
            next_node = head.next
            head.next = second
            second = second.next
            head.next.next = next_node
            head = next_node
        
    def reverse_list(self, head):
        if not head or not head.next:
            return head
        last = None
        while head:
            next_node = head.next
            head.next = last
            last = head
            head = next_node
        return last
        
