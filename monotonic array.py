class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        trail = nums[0]
        flag_inc = True
        flag_dec = True
        for index in range(len(nums)-1):
            if nums[index] > nums[index+1]:
                flag_inc = False
          
        for index in range(len(nums)-1):
            if nums[index] < nums[index+1]:
                flag_dec = False
        return flag_inc or flag_dec