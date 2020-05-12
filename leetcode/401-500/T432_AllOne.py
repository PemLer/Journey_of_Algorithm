class DlinkNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.pre = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.head = DlinkNode('', -1)
        self.tail = DlinkNode('', -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def __add_node(self, key) -> DlinkNode:
        node = DlinkNode(key, 1)
        next_node = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = next_node
        next_node.pre = node
        return node

    def __delete_node(self, node):
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        next_node.pre = pre_node

    def __increase(self, node):
        cur = node.next
        while cur != self.tail and cur.val == node.val:
            cur = cur.next
        if cur != node.next:
            node.pre.next = node.next
            node.next.pre = node.pre
            pre_node = cur.pre
            pre_node.next = node
            node.pre = pre_node
            node.next = cur
            cur.pre = node
        node.val += 1

    def __decrease(self, node):
        cur = node.pre
        while cur != self.head and cur.val == node.val:
            cur = cur.pre
        if cur != node.pre:
            node.pre.next = node.next
            node.next.pre = node.pre
            next_node = cur.next
            cur.next = node
            node.pre = cur
            node.next = next_node
            next_node.pre = node
        node.val -= 1

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.d:
            node = self.__add_node(key)
            self.d[key] = node
        else:
            node = self.d[key]
            self.__increase(node)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.d:
            node = self.d[key]
            if node.val == 1:
                self.__delete_node(node)
                self.d.pop(key)
            else:
                self.__decrease(node)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.tail.pre.key

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.head.next.key