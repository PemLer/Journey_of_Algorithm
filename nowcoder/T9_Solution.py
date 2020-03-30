# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        
    def push(self, node):
        self.stack_in.append(node)
        
    def pop(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
