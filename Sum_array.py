class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        difference = sum(nums2) - sum(nums1)
        ret = difference//len(nums1)
        return ret