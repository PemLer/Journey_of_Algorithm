import collections


class FreqStack:

    def __init__(self):
        self.count = collections.Counter()
        self.group = collections.defaultdict(list)
        self.max_count = 0

    def push(self, x: int) -> None:
        c = self.count[x] + 1
        self.count[x] = c
        self.group[c].append(x)
        if c > self.max_count:
            self.max_count = c

    def pop(self) -> int:
        value = self.group[self.max_count].pop()
        c = self.count[value] - 1
        self.count[value] = c
        if not self.group[self.max_count]:
            self.max_count -= 1
        return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()