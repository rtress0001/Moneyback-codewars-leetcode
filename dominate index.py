class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        #find the index of the maximum:
        max_num = max(nums)
        
        for i in range(len(nums)):
            if nums[i] == max_num:
                idx_max = i
        #check for max being twice a big as all other nums
        for num in nums:
            if num*2 > max_num and num != max_num:
                return -1
        
        return idx_max
                