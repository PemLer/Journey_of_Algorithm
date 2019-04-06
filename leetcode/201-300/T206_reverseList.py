# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        last = None
        while head:
            next_node = head.next
            head.next = last
            last = head
            head = next_node
        return last
        
