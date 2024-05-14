class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_num1 = 0
        for ele in nums1:
            if ele in nums2:
                count_num1+=1
        count_num2 = 0      
        for ele in nums2:
            if ele in nums1:
                count_num2+=1
                
        return [count_num1,count_num2]