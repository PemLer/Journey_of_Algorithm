class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.remain = capacity
        self.dict = collections.OrderedDict()        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        v = self.dict.pop(key)
        self.dict[key] = v
        return v        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.dict.pop(key)
            
        else:
            if self.remain > 0:
                self.remain -= 1                
            else:
                self.dict.popitem(last = False)
                
        self.dict[key] = value
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
