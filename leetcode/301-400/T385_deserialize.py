# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i].isdigit():
                tmp = ''
                while i < len(s) and s[i].isdigit():
                    tmp += s[i]
                    i += 1
                stack.append(NestedInteger(tmp))
            elif s[i] == '-':
                tmp = '-'
                i += 1
                while i < len(s) and s[i].isdigit():
                    tmp += s[i]
                    i += 1
                stack.append(NestedInteger(tmp))
            elif s[i] == ',':
                i += 1
                continue
            elif s[i] == ']':
                lst = []
                while stack and stack[-1] != '[':
                    lst.append(stack.pop())
                container = NestedInteger()
                while lst:
                    container.add(lst.pop())
                # 弹出'['
                stack.pop()
                stack.append(container)
                i += 1
        return stack[0]





