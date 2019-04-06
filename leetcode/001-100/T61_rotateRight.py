# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        k %= count
        if k == 0:
            return head
        
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        first = slow.next
        fast.next = head
        slow.next = None
        return first
            
        
