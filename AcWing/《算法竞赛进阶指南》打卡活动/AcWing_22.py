def get_input():
    """读取输入"""
    n = int(input())
    commands = [None] * n
    for i in range(n):
        try:
            items = input().split()
        except:
            continue
        if len(items) == 1:
            commands[i] = (items[0])
        else:
            commands[i] = (items[0], int(items[1]))
    return commands


class Editor:

    def __init__(self, commands):
        self.commands = commands
        self.stack_pre = []
        self.stack_post = []
        self.pre_sum = []
        self.max_pre = []
        # Ix D L R Qx

    def modify_pre_sum(self, value):
        if not self.pre_sum:
            self.pre_sum.append(value)
            self.max_pre.append(value)
        else:
            self.pre_sum.append(self.pre_sum[-1] + value)
            self.max_pre.append(max(self.max_pre[-1], self.pre_sum[-1]))

    def process(self):
        for com in self.commands:
            if com[0] == 'I':
                self.stack_pre.append(com[1])
                self.modify_pre_sum(com[1])
            elif com[0] == 'D':
                if self.stack_pre:
                    self.stack_pre.pop()
                    self.pre_sum.pop()
                    self.max_pre.pop()
            elif com[0] == 'L':
                if self.stack_pre:
                    self.stack_post.append(self.stack_pre.pop())
                    self.pre_sum.pop()
                    self.max_pre.pop()
            elif com[0] == 'R':
                if self.stack_post:
                    value = self.stack_post.pop()
                    self.stack_pre.append(value)
                    self.modify_pre_sum(value)
            else:
                print(self.max_pre[com[1] - 1])


commands = get_input()
editor = Editor(commands)
editor.process()



