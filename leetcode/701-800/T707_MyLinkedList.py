class DlinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque = []
        self.head = DlinkNode(-1)
        self.tail = DlinkNode(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def __add_node(self, base_node, node):
        # 加在base_node之前
        pre_node = base_node.pre
        pre_node.next = node
        node.pre = pre_node
        node.next = base_node
        base_node.pre = node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > len(self.deque) - 1:
            return -1
        return self.deque[index].val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = DlinkNode(val)
        if len(self.deque) > 0:
            self.__add_node(self.deque[0], node)
        else:
            self.__add_node(self.tail, node)
        self.deque.insert(0, node)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = DlinkNode(val)
        self.__add_node(self.tail, node)
        self.deque.append(node)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        node = DlinkNode(val)
        if index == len(self.deque):
            self.__add_node(self.tail, node)
            self.deque.append(node)
        elif index < 0:
            if len(self.deque) > 0:
                self.__add_node(self.deque[0], node)
            else:
                self.__add_node(self.tail, node)
            self.deque.insert(0, node)
        else:
            self.__add_node(self.deque[index], node)
            self.deque.insert(index, node)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > len(self.deque) - 1:
            return
        node = self.deque[index]
        node.pre.next = node.next
        node.next.pre = node.pre

        self.deque.pop(index)