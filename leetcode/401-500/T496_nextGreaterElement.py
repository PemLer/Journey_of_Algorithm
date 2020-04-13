from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
            elif nums2[i] > stack[-1]:
                while stack and nums2[i] > stack[-1]:
                    map[stack.pop()] = nums2[i]
                stack.append(nums2[i])
            elif nums2[i] <= stack[-1]:
                stack.append(nums2[i])

        while stack:
            map[stack.pop()] = -1

        res = []
        for num in nums1:
            res.append(map[num])
        return res


if __name__ == '__main__':
    sol = Solution()
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    print(sol.nextGreaterElement(nums1, nums2))
