# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一 栈
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        stack = []
        while True:
            count = k
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1

            if count:
                p.next = head
                break

            while stack:
                p.next = stack.pop()
                p = p.next

            p.next = tmp
            head = tmp

        return dummy.next

# 方法二 递归
class Solution2:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head
