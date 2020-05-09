class DlinkNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.pre = None


class Dlink:
    def __init__(self):
        self.head = DlinkNode(-1, -1)
        self.tail = DlinkNode(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def is_empty(self):
        return self.head.next == self.tail

    def add_node(self, node):
        last = self.tail.pre
        last.next = node
        node.pre = last
        self.tail.pre = node
        node.next = self.tail

    def delete_node(self):
        delete_node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.pre = self.head
        return delete_node


class LFUCache:

    def __delete_node(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        self.key_dic.pop(node.key)

    def __add_node(self, freq, node):
        if freq in self.freq_dic:
            self.freq_dic[freq].add_node(node)
        else:
            self.freq_dic[freq] = Dlink()
            self.freq_dic[freq].add_node(node)

    def __init__(self, capacity: int):
        self.freq_dic = {}
        self.key_dic = {}
        self.capacity = capacity
        self.count = 0
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_dic:
            return -1
        else:
            node = self.key_dic[key]
            freq = node.freq
            self.__delete_node(node)
            node.freq += 1
            if self.min_freq == freq and self.freq_dic[self.min_freq].is_empty():
                self.min_freq += 1
            self.__add_node(freq + 1, node)
            self.key_dic[key] = node
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_dic:
            node = self.key_dic[key]
            freq = node.freq
            self.__delete_node(node)
            if self.min_freq == freq and self.freq_dic[freq].is_empty():
                self.min_freq += 1
            node.freq += 1
            node.value = value
            self.__add_node(freq + 1, node)
            self.key_dic[key] = node
        else:
            if self.capacity == 0:
                return
            if self.count == self.capacity:
                delete_node = self.freq_dic[self.min_freq].delete_node()
                self.key_dic.pop(delete_node.key)
            else:
                self.count += 1
            node = DlinkNode(key, value)
            self.__add_node(1, node)
            self.key_dic[key] = node
            self.min_freq = 1