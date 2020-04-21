import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict()
        self.lst = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dic:
            self.lst.append(val)
            self.dic[val] = len(self.lst) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dic:
            index = self.dic.pop(val)
            self.lst[index], self.lst[len(self.lst) - 1] = self.lst[len(self.lst) - 1], self.lst[index]
            if self.lst[index] in self.dic:
                self.dic[self.lst[index]] = index
            self.lst.pop()
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0, len(self.lst) - 1)
        # self.lst[index], self.lst[len(self.lst) - 1] = self.lst[len(self.lst) - 1], self.lst[index]
        # val = self.lst.pop()
        # self.dic.pop(val)
        return self.lst[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == '__main__':
    # ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
    # [[],[0],[1],[0],[2],[1],[]]
    # ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
    # [[],[0],[0],[0],[],[0],[0]]
    res = []
    rs = RandomizedSet()
    res.append(rs.remove(0))
    res.append(rs.remove(0))
    res.append(rs.insert(0))
    res.append(rs.getRandom())
    res.append(rs.remove(0))
    res.append(rs.insert(0))
    print(res)

