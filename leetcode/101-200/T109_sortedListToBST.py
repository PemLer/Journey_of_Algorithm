# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        pre = slow = fast = head
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)

        while slow.next and fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        left,right = head,slow.next
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root


