class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            i = nums2.index(num)
            x = None
            for v in nums2[i:]:
                if v > num:
                    x = v
                    break
            res.append(x) if x else res.append(-1)
        return res
