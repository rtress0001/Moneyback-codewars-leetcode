class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return nums[0]
    
        for ele in nums:
            if nums.count(ele) == 1:
                return ele
            else:
                continue