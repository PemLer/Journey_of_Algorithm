# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            pre = head
            temp = pre
            cur = head.next
            new = ListNode(0)
            first = new
            cou = 0
            while cur:
                if pre.val == cur.val:
                    cur = cur.next
                    cou += 1
                    #pre.next = None
                else:
                    if cou != 0:
                        pre = cur
                        cur = cur.next
                        cou = 0
                    else:
                        new.next = pre
                        new = new.next
                        #new.next = None
                        temp = pre
                        pre = pre.next
                        cur = cur.next
            if pre.next == None:
                new.next = pre
            if cou != 0:
                temp.next = None
            return first.next
        
