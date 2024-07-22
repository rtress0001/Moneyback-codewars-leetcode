class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        #sorting the array
        nums.sort()
        
        #intilizing a minimum
        max_min = 0
        
        #creating a pointer for next values
        end_pointer = len(nums)-1
        pointer = 0
        
        #creating a half loop with a while loop
        while end_pointer>pointer:
            max_min = max(nums[end_pointer]+nums[pointer],max_min)
            end_pointer -= 1
            pointer += 1
        
        return max_min
        