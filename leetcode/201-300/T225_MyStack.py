class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_in = []
        self.queue_out = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue_in.append(x)
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue_in) > 1:
            self.queue_out.append(self.queue_in.pop(0))
        tmp = self.queue_in.pop(0)
        while self.queue_out:
            self.queue_in.append(self.queue_out.pop(0))
        return tmp
        
    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue_in[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if not self.queue_in and not self.queue_out:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
