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
        num1 = num2 = 0
        while l1 or l2:
            if l1:
                num1 = num1*10 + l1.val
                l1 = l1.next
            if l2:
                num2 = num2*10 + l2.val
                l2 = l2.next
        num = num1 + num2
        l = len(str(num))
        ans = head = ListNode(-1)
        for i in range(l-1,-1,-1):
            node = ListNode(num//(10**i))
            num = num - 10**i*(num//(10**i))
            head.next = node
            head = head.next
        return ans.next

