class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        max_num = -1
        for ele in nums:
            if ele > 0 and -ele in nums:
                if ele > max_num:
                    max_num = ele
            
        if max_num:
            return max_num
        else:
            return -1