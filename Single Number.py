class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        single = 0
        for ele in nums:
            if nums.count(ele) == 1:
                return ele