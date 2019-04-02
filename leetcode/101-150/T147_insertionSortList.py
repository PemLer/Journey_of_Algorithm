# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        while head:
            next_node = head.next
            p = dummy
            while p.next and p.next.val < head.val:
                p = p.next
            head.next = p.next
            p.next = head
            head = next_node
        return dummy.next            
        
