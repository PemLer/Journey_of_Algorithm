import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.lst.append(val)
        b = val not in self.dic
        if val in self.dic:
            self.dic[val].add(len(self.lst) - 1)
        else:
            self.dic[val] = {len(self.lst) - 1}
        return b

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        b = val in self.dic
        if val in self.dic:
            index = self.dic[val].pop()
            if not self.dic[val]:
                self.dic.pop(val)
            if index == len(self.lst) - 1:
                if self.lst[index] in self.dic:
                    self.dic[self.lst[index]].discard(len(self.lst) - 1)
                    if not self.dic[self.lst[index]]:
                        self.dic.pop(self.lst[index])
                self.lst.pop()
            else:
                self.lst[index], self.lst[-1] = self.lst[-1], self.lst[index]
                self.dic[self.lst[index]].discard(len(self.lst) - 1)
                self.dic[self.lst[index]].add(index)
                self.lst.pop()
        return b

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        index = random.randint(0, len(self.lst) - 1)
        return self.lst[index]


if __name__ == "__main__":
    rc = RandomizedCollection()
    rc.insert(4)
    print(rc.dic, rc.lst)
    rc.remove(4)
    print(rc.dic, rc.lst)
    rc.insert(4)
    print(rc.dic, rc.lst)