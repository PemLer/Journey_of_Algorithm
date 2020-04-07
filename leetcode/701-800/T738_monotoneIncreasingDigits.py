class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        寻找原数组中不满足递增的数的前一位
        """
        arr = list(map(int, list(str(N))))

        index = -1
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                while i > 0:
                    if arr[i] == arr[i-1]:
                        index = i - 1
                        i -= 1
                    else:
                        break
                if index == -1:
                    index = i
                break

        if index != -1:
            arr[index] -= 1
            for i in range(index+1, len(arr)):
                arr[i] = 9

        return int(''.join(map(str, arr)))


if __name__ == '__main__':
    sol = Solution()
    print(sol.monotoneIncreasingDigits(10))
