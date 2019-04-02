# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        jin = 0

        while l1 != None and l2 != None:
            temp = l1.val + l2.val + jin
            jin = temp//10
            head.next = ListNode(temp%10)
            l1 = l1.next
            l2 = l2.next
            head = head.next
        while l1 != None:
            temp = l1.val + jin
            jin = temp//10
            head.next = ListNode(temp%10)
            l1 = l1.next
            head = head.next
        while l2 != None:
            temp = l2.val + jin
            jin = temp // 10
            head.next = ListNode(temp % 10)
            l2 = l2.next
            head = head.next
        if jin != 0:
            head.next = ListNode(jin)
            head = head.next
        return first.next

