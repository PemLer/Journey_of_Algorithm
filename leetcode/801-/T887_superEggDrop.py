import time

class Solution:
    cache = {}

    def superEggDrop(self, K: int, N: int) -> int:
        if N == 0:
            return 0
        elif K == 1:
            return N

        key = N * 1000 + K
        if key in self.cache:
            return self.cache[key]

        low, high = 1, N
        while low + 1 < high:
            mid = low + high >> 1
            low_val = self.superEggDrop(K-1, mid-1)
            high_val = self.superEggDrop(K, N-mid)

            if low_val < high_val:
                low = mid
            elif low_val > high_val:
                high = mid
            else:
                low = high = mid

        minimum = 1 + min(
            max(self.superEggDrop(K-1, low-1), self.superEggDrop(K, N-low)),
            max(self.superEggDrop(K-1, high-1), self.superEggDrop(K, N-high))
            )
        self.cache[key] = minimum
        return minimum


if __name__ == '__main__':
    sol = Solution()
    start_time = time.time()
    print(sol.superEggDrop(3, 20))
    print('cost:', time.time() - start_time)
