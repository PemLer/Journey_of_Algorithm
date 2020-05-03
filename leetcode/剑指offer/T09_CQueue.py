class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(value)
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        else:
            return -1



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()