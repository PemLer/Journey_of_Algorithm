class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if numbers[0] < numbers[-1] or len(numbers) == 1:
            return numbers[0]

        l, r = 0, len(numbers)
        while l < r and numbers[l] == numbers[-1]:
            l += 1

        while l < r:
            mid = l + r >> 1
            if numbers[mid] > numbers[-1]:
                l = mid + 1
            else:
                r = mid

        return numbers[l] if l < len(numbers) else numbers[0]