# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        length1 = 0
        length2 = 0
        root1 = pHead1
        root2 = pHead2
        while root1:
            length1 += 1
            root1 = root1.next
        while root2:
            length2 += 1
            root2 = root2.next
        if length1 > length2:
            for _ in range(length1-length2):
                pHead1 = pHead1.next
            return pHead1.val
        else:
            for _ in range(length2-length1):
                pHead2 = pHead2.next
            return pHead2.val

if __name__ == '__main__':
    sol = Solution()
    a1 = [x for x in range(1, 10)]
    root = ListNode(0)
    cur = root
    for i in a1:
        tmp = ListNode(i)
        cur.next = tmp
        cur = cur.next
    root2 = root.next.next.next
    print(sol.FindFirstCommonNode(root, root2))