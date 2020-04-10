# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.lst = self.flatten(nestedList)
        self.index = 0

    def flatten(self, lst):
        res = []
        for item in lst:
            if item.isInteger():
                res.append(item)
            else:
                res.extend(self.flatten(item.getList()))
        return res

    def next(self) -> int:
        if self.hasNext:
            value = self.lst[self.index]
            self.index += 1
            return value

    def hasNext(self) -> bool:
        return self.index != len(self.lst)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())