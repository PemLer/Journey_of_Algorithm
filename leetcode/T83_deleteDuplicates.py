# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast:
            if fast.val == slow.val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
        return head
        
