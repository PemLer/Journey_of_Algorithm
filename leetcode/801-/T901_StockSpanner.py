class StockSpanner:

    def __init__(self):
        self.data = []
        self.stack = []
        self.cnt = 0

    def next(self, price: int) -> int:
        if not self.stack or self.data[self.stack[-1]] > price:
            self.stack.append(self.cnt)
            self.data.append(price)
            self.cnt += 1
            return 1
        else:
            while self.stack and self.data[self.stack[-1]] <= price:
                self.stack.pop()
            if self.stack:
                res = self.cnt - self.stack[-1]
                self.stack.append(self.cnt)
                self.data.append(price)
                self.cnt += 1
                return res
            else:
                res = self.cnt + 1
                self.stack.append(self.cnt)
                self.data.append(price)
                self.cnt += 1
                return res


# 简化版本
class StockSpanner2:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight
