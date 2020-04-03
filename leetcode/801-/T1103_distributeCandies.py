from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        i = 0
        res = [0] * num_people
        while candies > 0:
            if i + 1 <= candies:
                res[i % num_people] += i + 1
                candies -= i + 1
            else:
                res[i % num_people] += candies
                candies = 0
            i += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    items = [
        [7, 4],
        [10, 3]
    ]
    for item in items:
        print(sol.distributeCandies(*item))
