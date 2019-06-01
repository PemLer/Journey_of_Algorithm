class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center
        

    def randPoint(self) -> List[float]:
        l = self.r * math.sqrt(random.random())
        theta = 360 * random.random() / (2 * math.pi)
        return [self.x+l*math.cos(theta), self.y+l*math.sin(theta)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
