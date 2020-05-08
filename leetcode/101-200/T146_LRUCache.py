import collections


# 方法一 有序字典
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        else:
            if self.capacity == len(self.dic):
                self.dic.popitem(last=False)
        self.dic[key] = value


# 方法二 双向链表
class LinkNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = LinkNode(-1, -1)
        self.tail = LinkNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.dic = {}

    def move_to_end(self, node):
        pre_node = node.pre
        next_node = node.next
        pre_node.next = next_node
        next_node.pre = pre_node
        self.add_node(node)
        self.dic[node.key] = node

    def add_node(self, new_node):
        last_two = self.tail.pre
        last_two.next = new_node
        new_node.pre = last_two
        new_node.next = self.tail
        self.tail.pre = new_node

    def get(self, key: int) -> int:
        if key in self.dic:
            self.move_to_end(self.dic[key])
            return self.dic[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].value = value
            self.move_to_end(self.dic[key])
        else:
            new_node = LinkNode(key, value)
            if self.count == self.capacity:
                delete_node = self.head.next
                self.dic.pop(delete_node.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
            else:
                self.count += 1
            self.add_node(new_node)
            self.dic[key] = new_node