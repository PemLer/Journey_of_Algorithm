from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1

        stack = []
        res = [0] * n
        index = 0
        while head:
            while stack and head.val > stack[-1][1]:
                i, v = stack.pop()
                res[i] = head.val
            stack.append([index, head.val])
            index += 1
            head = head.next

        return res
