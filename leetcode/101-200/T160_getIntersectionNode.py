# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1, len2 = 0, 0
        curA, curB = headA, headB
        while curA:
            curA = curA.next
            len1 += 1
        while curB:
            curB = curB.next
            len2 += 1
            
        if len1 > len2:
            for _ in range(len1-len2):
                headA = headA.next
        else:
            for _ in range(len2-len1):
                headB = headB.next
        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
