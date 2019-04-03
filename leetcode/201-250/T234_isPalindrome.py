# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        else:
            slow = head
            fast = head
            while fast.next != None and fast.next.next != None:
                slow = slow.next
                fast = fast.next.next
            med = slow
            cur = med.next
            new = None
            while cur:
                temp = cur.next
                cur.next = new
                new = cur
                cur = temp
            while new:
                if head.val == new.val:
                    print(1)
                    head = head.next
                    new = new.next
                else:
                    return False
            return True
