# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        new_node = ListNode(-1)
        new_node.next = head
        pre = new_node
        count = 0
        for _ in range(m-1):
            pre = pre.next
        cur = pre.next
        next_node = cur.next
        for _ in range(n-m):
            cur.next = next_node.next
            next_node.next = pre.next
            pre.next = next_node
            next_node = cur.next
        return new_node.next
        
