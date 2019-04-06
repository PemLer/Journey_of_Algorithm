"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        first = cur = head
        # step 1 复制节点
        while head:
            new_node = Node(head.val, None, None)
            next_node = head.next
            head.next = new_node
            new_node.next = next_node
            head = next_node
        
        # step 2 复制随机指针
        while first:
            if first.random:
                first.next.random = first.random.next
            first = first.next.next
            
        # step 3 断开链表
        copy = new = Node(-1, None, None)
        while cur:
            next_node = cur.next
            cur.next = next_node.next
            new.next = next_node
            cur = cur.next
            new = new.next
        return copy.next
        
